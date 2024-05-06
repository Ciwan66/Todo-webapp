from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView ,LogoutView
from django.views.generic import View
from .models import CustomUser
from .forms import RegisterForm,LoginForm
# Create your views here.

class RegisterView(View):
    template_name = 'accounts/register.html'
    model = CustomUser
    form_class = RegisterForm
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):

        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('users_login')



class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    redirect_authenticated_user =True
    

