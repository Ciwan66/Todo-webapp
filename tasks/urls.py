from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('task/',views.TaskList.as_view(),name="task_list"),
    path('task/create',views.TaskCreate.as_view(),name="task_create"),
    path('task/<pk>/detail',views.TaskDetail.as_view(),name="task_detail"),
    path('task/<pk>/delete',views.TaskDelete.as_view(),name="task_delete"),
    path('task/<pk>/update',views.TaskUpdate.as_view(),name="task_update"),
]
