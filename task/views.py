from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from django.views import View
from django.http import JsonResponse


class Index(View):
    def get(self, request):
        tasks = get_object_or_404(Task)
        return render(request, 'task/index.html', {'tasks': tasks})


def api(request):
    def get(self, request, pk):
        tasks = Task.objects.all()
        data = {'tasks': list(tasks.values())}
        return JsonResponse(data)
    
class Add_task(View):
    def post(self, request):
        task = Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            done=request.POST['done']
        )
        return JsonResponse({'task': task.to_dict()})
    
def task_add(request):
    if request.method == 'POST':
        task = Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            done=request.POST['done']
        )
        return redirect('index')
    return render(request, 'task/task_add.html')
# Create your views here.
