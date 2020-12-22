from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList
# Create your views here.

def index(request):
    # return HttpResponse("Hello")
    # return redirect("index")
    tasks=TaskList.objects.all()
    for task in tasks:
        print(task.task)
    return render(request, "index.html", { "tasks":tasks})

def taskSubmit(request):
    taskName=request.POST.get("taskname")
    task = TaskList(task=taskName) 
    task.save()
    tasks=TaskList.objects.all()
    return render(request, "index.html", { "tasks":tasks})

def taskDelete(request):
    entry= TaskList.objects.get(id=request.POST.get("id"))
    entry.delete()
    tasks=TaskList.objects.all()
    return render(request, "index.html", { "tasks":tasks})