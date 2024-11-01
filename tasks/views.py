from django.shortcuts import render ,get_object_or_404
from .models import Task

def task_main(request):
    return render(request, 'tasks/task/main.html')
def task_list(request):
    tasks = Task.objects.all()
    return render(
        request,
        'tasks/task/list.html',
        {'tasks': tasks}
    )
def task_completed(request):
    tasks_completed=Task.completed.all()

    return render(
        request,
        'tasks/task/completed_list.html',
        {'tasks': tasks_completed}
    )


def task_detail(request, task_id):
    # try:
    #     task = Task.objects.get(id=task_id)
    #
    # except Task.DoesNotExist:
    #     raise Http404("Task not found")

    task = get_object_or_404(Task, id=task_id, is_completed=True )

    return render(
        request,
        'tasks/task/detail.html',
        {'task': task}
    )

def task_detail_all(request, task_id):
    # try:
    #     task = Task.objects.get(id=task_id)
    #
    # except Task.DoesNotExist:
    #     raise Http404("Task not found")

    task = get_object_or_404(Task, id=task_id )

    return render(
        request,
        'tasks/task/detail.html',
        {'task': task}
    )