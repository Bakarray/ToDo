from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'description', 'due_date', 'progress']
