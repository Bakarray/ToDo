from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


# views are python functions that receives an HTTP request object, and returns an http response object
@login_required(login_url="login")
def home_page(request):
    user = request.user
    
    user_tasks = user.task_set.all()
    

    context = {"user_tasks": user_tasks, 'user': user}

    return render(request, 'task_manager/index.html', context)


@login_required(login_url="login")
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()
            return redirect('home_page')
    else:
        form = TaskForm()

    context = {"form": form}
    return render(request, 'task_manager/create_task.html', context)


@login_required(login_url="login")
def description(request, task_id):
    for task in Task.objects.all():
        if task.id == task_id:
            context = {'task': task}
    try:
        context
    except:
        raise Http404("Task does not exist")
    
    return render(request, 'task_manager/task_desc.html', context)


def user_login(request):
    page = "login"
    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return render(request, 'task_manager/auth.html', context)   

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'username or password incorrect')
            
    return render(request, 'task_manager/auth.html', context)


def user_signup(request):
    page = "signup"
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()
            messages.success(request, "Signup successful, you can login now")
            return redirect('login')
        else:
            messages.error(request, "please correct the error below")

    else:
        form = UserCreationForm()

    context = {'page': page, "form": form}
    return render(request, 'task_manager/auth.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')