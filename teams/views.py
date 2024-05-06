from django.shortcuts import render
from django.views.generic import View , ListView, DeleteView, UpdateView ,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TeamList(LoginRequiredMixin,ListView):
    pass
class TeamDetail(LoginRequiredMixin,ListView):
    pass
class TeamCreate(LoginRequiredMixin,CreateView):
    pass
class TeamDelete(LoginRequiredMixin,DeleteView):
    pass
class TeamUpdate(LoginRequiredMixin,UpdateView):
    pass


