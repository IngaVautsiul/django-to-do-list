from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title':'Главная страница сайта', 'tasks': tasks})
    
# Create your views here.
def about(request):
    return render(request, 'main/about.html')
    
    
# Create your views here.
def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
    