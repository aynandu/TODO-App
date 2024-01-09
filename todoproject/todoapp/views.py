from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .form import ToDOForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
class ToDoListView(ListView):
    model = task
    template_name = 'index.html'
    context_object_name = 'task'

class ToDoDetailView(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'task'

class ToDoUpdateView(UpdateView):
    model = task
    template_name = 'edit.html'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})
class ToDoDeleteView(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

def add(request):
    Task=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        data=task(name=name,priority=priority,date=date)
        data.save()
    return render(request,'index.html',{'task':Task})

#def details(request):
#    Task=task.objects.all()
#   return render(request,'details.html',{'task':Task})

def delete(request,taskid):
    Task=task.objects.get(id=taskid)
    if request.method=='POST':
        Task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    Task=task.objects.get(id=id)
    frm=ToDOForms(request.POST or None,instance=Task)
    if frm.is_valid():
        frm.save()
        return redirect('/')
    return render(request,'update.html',{'task':Task,'frm':frm})
