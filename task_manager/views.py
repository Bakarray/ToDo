from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# views are python functions that receives an HTTP request object, and returns an http response object
def home_page(request):
    context = {}
    task_list = Task.objects.all()
    context = {"task_list": task_list}

    return render(request, 'task_manager/index.html', context)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = TaskForm()

    context = {"form": form}
    return render(request, 'task_manager/create_task.html', context)
    