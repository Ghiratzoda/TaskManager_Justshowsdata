from django.shortcuts import render
from .models import Tasks
# Create your views here.

def tasks_list(request):
    tasks = Tasks.objects.all()
    context = {'all_tasks': tasks}
    return render(request, "tasks/all_taks.html", context)

    

