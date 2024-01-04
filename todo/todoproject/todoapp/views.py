from django.shortcuts import render,redirect

from .forms import TodoForm
from . models import Todo


# Create your views here.
def index(request):
    return render(request,'index.html')
def add(request):
    tasks = Todo.objects.all()
    if request.method=="POST":
        taskname=request.POST.get('taskname','')
        taskpriority = request.POST.get('taskpriority', '')
        taskdate = request.POST.get('taskdate', '')

        task=Todo(taskname=taskname,taskpriority=taskpriority,taskdate=taskdate)
        task.save()

    return render(request,'index.html',{'tasks':tasks})
def update(request,id):
    eachtask=Todo.objects.get(id=id)
    form=TodoForm(request.POST or None,request.FILES,instance=eachtask)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'eachtask':eachtask})
def delete(request,id):
    if request.method=='POST':
        dtask=Todo.objects.get(id=id)
        dtask.delete()
        return redirect('/')
    return render(request,'delete.html')


