from django.shortcuts import render , redirect
from django.views.generic import View , ListView, DeleteView, UpdateView ,CreateView ,DetailView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import TeamMemberMixin,TeamOwnerMixin
from .models import Team
from .forms import TeamForm , AddMemberForm
from django.db.models import Q
from django.urls import reverse_lazy,reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from accounts.models import CustomUser
from tasks.views import TaskList
from tasks.models import Task


# Create your views here.

class TeamList(LoginRequiredMixin,ListView):
    model = Team
    template_name = 'teams/team_list.html'
    context_object_name = 'teams'
    
    def get_queryset(self):
        return Team.objects.filter(Q(owner = self.request.user)| Q(members = self.request.user) )
    

class TeamDetail(LoginRequiredMixin,DetailView):
    model = Team
    template_name = 'teams/team_detail.html'
    context_object_name = 'team'


class TeamCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Team
    form_class =TeamForm
    template_name ='teams/team_create.html'
    success_url= reverse_lazy('team_list')
    success_message = "Team Created"
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        obj.members.add(self.request.user) 
        return super().form_valid(form)
    


class TeamDelete(LoginRequiredMixin,TeamOwnerMixin,SuccessMessageMixin,DeleteView):
    model =Team
    success_url = reverse_lazy('team_list')
    success_message = 'Team deleted successfully'
    def get (self ,request , pk):
        return redirect('team_list')
    
class TeamUpdate(LoginRequiredMixin,TeamOwnerMixin,SuccessMessageMixin,UpdateView):
    model=Team
    form_class = TeamForm
    template_name = 'teams/team_update.html'
    success_message = 'Team Updated successfully'
    
    def get_success_url(self) :
        pk = self.object.pk
        return reverse('team_detail',kwargs={'pk':pk})

class TeamAddMember(LoginRequiredMixin, View):
    template_name = 'teams/team_add_member.html'
    form_class = AddMemberForm
    success_url = reverse_lazy('team_list')

    def get(self, request, pk):
        team = Team.objects.get(id=pk)
        available_users = CustomUser.objects.exclude(id__in=team.members.all().values_list('id', flat=True))
        if available_users.exists():
            form = self.form_class()
            context = {'form': form, 'team': team, 'available_users': available_users}
            return render(request, self.template_name, context)
        else:
            messages.info(request, 'There are no users available to add.')
            return redirect('team_detail', pk=pk)
    
    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            members = form.cleaned_data['members']
            team = Team.objects.get(id=pk)
            team.members.add(*members)
            messages.success(request, 'Members added successfully.')
            return redirect('team_detail', pk=pk)
        else:
            return render(request, self.template_name, {'form': form, 'team_id': pk})
        


class TeamTaskList(TaskList):
    def get_queryset(self):
        team_id = self.kwargs['pk']
        team=Team.objects.get(pk=team_id)
        return Task.objects.filter(team=team)
    

    