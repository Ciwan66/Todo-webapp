from django.urls import path
from . import views
urlpatterns = [
    path('',views.TeamList.as_view(),name='team_list'),
    path('create',views.TeamCreate.as_view(),name='team_create'),
    path('<pk>/delete',views.TeamDelete.as_view(),name='team_delete'),
    path('<pk>/detail',views.TeamDetail.as_view(),name='team_detail'),
    path('<pk>/update',views.TeamUpdate.as_view(),name='team_update'),
    path('<pk>/add_member/',views.TeamAddMember.as_view(),name='team_add_member'),

    #############
    path('<int:pk>/team_task_list',views.TeamTaskList.as_view(),name='team_task_list'),
    path('<int:pk>/team_task_create',views.TeamTaskCreate.as_view(),name='team_task_create'),
    path('<int:team>/<int:pk>/team_task_detail',views.TeamTaskDetail.as_view(),name='team_task_detail'),

]
