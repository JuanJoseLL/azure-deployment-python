from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject
# Create your views here.

def index(request):
    title = "Django course !!"
    return render(request, 'index.html', {
        'title':title
    })


def about(request):
    username = 'juan'
    return render(request, 'about.html',{
        'username':username
    })


def hello(request, username):
    return HttpResponse("<h1> Hello %s </h1>" %username)




def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })


def tasks(request):
   # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html',{
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
        #Hola
    else:
        Task.objects.create(tittle=request.POST['title'],
                            description=request.POST['description'],
                            projects_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        redirect('projects')


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(projects_id=id)
    return render(request, 'detail.html', {
        'project': project,
        'tasks': tasks
    })

