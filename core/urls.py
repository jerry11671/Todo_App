from django.urls import path
from .views import TaskCreate, TaskDetail, TaskDelete, TaskList, get_incomplete_task

urlpatterns = [
    path('task_list/<int:pk>/', TaskList.as_view(), name='task-list'),
    path('task_create/', TaskCreate.as_view(), name='task-create'),
    path('task_detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('<int:pk>/incomplete_tasks/', get_incomplete_task, name='incomplete_task'),
]