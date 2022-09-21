from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.
def show_watchlist(request):
    return render(request, "mywatchlist.html", context)

data_watchlist = MyWatchList.objects.all()
context = {
    'list_mywatchlist': data_watchlist,
    'nama': 'Dhina Rotua Mutiara',
    'student_ID': '2106702182'
}

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request,id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")