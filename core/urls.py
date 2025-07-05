from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('tasks/next/', views.get_next_task, name='get_next_task'),
    path('tasks/<int:pk>/update/', views.update_task_status, name='update_task_status'),
] 