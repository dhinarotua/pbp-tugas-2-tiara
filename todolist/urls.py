# Implement Routings Here
from audioop import add
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import status
from todolist.views import delete
from todolist.views import show_json_by_id
from todolist.views import add_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('change/<int:id>', status, name='status'),
    path('delete/<int:id>', delete, name='delete'),
    path('json', show_json_by_id, name='show_json_by_id'),
    path('add-task/', add_task, name='add_task'),
]