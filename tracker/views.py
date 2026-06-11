from django.shortcuts import render

from .models import Task

# Create your views here.

def home(request):

    total_tasks = Task.objects.count()

    pending_tasks = Task.objects.filter(status="Pending").count()

    completed_tasks = Task.objects.filter(status="Completed").count()

    context = {
        'total_tasks': total_tasks,
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks
    }

    return render(request, 'home.html', context)

def add_task(request):

    if request.method == "POST":
        task_name = request.POST.get("task_name")
        description = request.POST.get("description")
        priority = request.POST.get("priority")
        status = request.POST.get("status")

        Task.objects.create(
            task_name=task_name,
            description=description,
            priority=priority,
            status=status
        )

    return render(request, 'add_task.html')

def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'view_tasks.html', {'tasks': tasks})

def about(request):
    return render(request, 'about.html')