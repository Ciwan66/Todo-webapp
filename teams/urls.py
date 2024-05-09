from django.urls import path
from .views import TeamList,TeamDelete,TeamDetail,TeamUpdate,TeamCreate,TeamAddMember,TeamTaskList,TeamTaskCreate
urlpatterns = [
    path('',TeamList.as_view(),name='team_list'),
    path('create',TeamCreate.as_view(),name='team_create'),
    path('<pk>/delete',TeamDelete.as_view(),name='team_delete'),
    path('<pk>/detail',TeamDetail.as_view(),name='team_detail'),
    path('<pk>/update',TeamUpdate.as_view(),name='team_update'),
    path('<int:pk>/team_task_list',TeamTaskList.as_view(),name='team_task_list'),
    path('<int:pk>/team_task_create',TeamTaskCreate.as_view(),name='team_task_create'),
    path('<pk>/add_member/',TeamAddMember.as_view(),name='team_add_member'),
]
