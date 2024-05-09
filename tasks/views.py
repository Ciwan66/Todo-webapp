from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Task
from .forms import TaskForm
from django.urls import reverse , reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .mixins import OwnerMixin

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    

class TaskCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = 'tasks/task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    success_message='Task Created'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user

        return super().form_valid(form)
    

class TaskDetail(LoginRequiredMixin,OwnerMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "tasks/task_detail.html"
    

class TaskDelete(LoginRequiredMixin, OwnerMixin,SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    success_message= "Task Deleted Successfuly"

class TaskUpdate(LoginRequiredMixin,OwnerMixin,SuccessMessageMixin,UpdateView):
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    model = Task
    success_message="Task Updated"
    def get_success_url(self):
        pk = self.object.pk
        return reverse('task_detail' , kwargs={'pk':pk})
