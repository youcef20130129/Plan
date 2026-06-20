from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    tasks=Task.objects.all()
    search_query=request.POST.get('search')
    if search_query:
        tasks=Task.objects.filter(title__contains=search_query)
    context={'tasks':tasks}
    return render(request,'todos/base.html',context)

def create_task(request):
    if request.method=='POST':
        title=request.POST.get('title')
        Task.objects.create(title=title)
    return redirect('list-tasks')

def delete_task(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('list-tasks')

def update_task(request,id):
    task=Task.objects.get(id=id)
    context={'task':task}
    if request.method=='POST':
        newTitle=request.POST.get('title')
        task.title=newTitle
        task.save()
        return redirect('list-tasks')
    return render(request,'todos/edit-task.html',context)

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        if password!=password2:
            return HttpResponse('Passwords do not match')
        else:
            User.objects.create_user(username=username,email=email,password=password)
            return redirect('login')
    return render(request,'todos/register.html')