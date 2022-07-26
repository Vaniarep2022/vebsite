from main. forms import TaskForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    task = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': 'title'})

def about(request):
    return render(request, 'main/about.html')

def storm(request):
    return HttpResponse('<h1>Что на сегодня?</h1>')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была не верной'

    form = TaskForm()
    context ={
        'form':form,
        'error': error
    }
    return create(request, 'main/create.html')