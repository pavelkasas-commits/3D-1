from django import views
from django.urls import path

from .views import TaskCreateView, TaskDeleteView, TaskDetailView, TaskListView, TaskUpdateView, SignUpView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("new/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path('signup/', SignUpView.as_view(), name='signup'),

]
