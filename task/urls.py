from django.urls import path
from . import views
from .views import Index, Add_task, task_add

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('task_add/', task_add, name='task_add'),
    path('add_task/', Add_task.as_view(), name='add_task'),
    #path('api/', views.api, name='api'),
]
