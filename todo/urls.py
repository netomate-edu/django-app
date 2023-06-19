from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_todo, name='add_todo'),
    path('remove/<int:todo_id>', views.remove_add, name='remove_todo'),
    
]
