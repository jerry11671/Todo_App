from .models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    # num_incomplete_task = serializers.IntegerField()
    class Meta:
        model = Task
        fields = "__all__"
        # exclude = ['user']
