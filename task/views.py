from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from .forms import Task_form
from django.views import View
from django.http import JsonResponse


class Index(View):
    def get(self, request):
        tasks = Task.objects.all()
        form = Task_form()
        if request.method == 'POST':
            form = Task_form(request.POST)
            if form.is_valid():
                form.save()
            return redirect('index')
        
        context = {'tasks': tasks, 'form': form}
        return render(request, 'task/index.html', context)
    


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
