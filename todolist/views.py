import datetime
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.create_form import TaskForm
from django.http import HttpResponse
from django.core import serializers
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user = request.user)
    context = {
        'list_task': data_task,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            Task.objects.create(title=title, description=description, date=datetime.datetime.now(), user=request.user)
            return redirect('todolist:show_todolist')
    else:
        form = TaskForm()
        
    context = {'form':form}
    return render(request, 'create-task.html', context)

@login_required(login_url='/todolist/login/')
def status(request, id):
    task = Task.objects.get(id = id)
    task.is_finished = not(task.is_finished)
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    return redirect('todolist:show_todolist')

def show_json_by_id(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(title=title, description=description,date=datetime.date.today(), is_finished=False, user=request.user)

        context = {
            'fields':{
                'title':task.title,
                'description':task.description,
                'is_finished':task.is_finished,
                'date':task.date,
            },
            'pk':task.pk
        }
        
        return JsonResponse(context)