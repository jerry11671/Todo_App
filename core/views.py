from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework import generics
from .models import Task
# from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import filters

class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
        
class TaskList(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title']
    
    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    

@api_view(['GET',])
def get_incomplete_task(request, pk):
    user = request.user
    task = Task.objects.filter(user=user)
    print(task)
    num_of_incomplete_task = task.filter(completed=False).count()
    return Response({
        'num_of_incomplete_task': num_of_incomplete_task
    })    

class TaskDetail(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


