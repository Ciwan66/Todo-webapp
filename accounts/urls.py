from django.urls import path , include
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import re_path

urlpatterns = [
    path('login/',views.CustomLoginView.as_view(),name="users_login"),
    path('signup/',views.RegisterView.as_view(),name="users_register"),
    path('logout/',LogoutView.as_view(next_page="index"),name='users_logout'),

]
