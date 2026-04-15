from django.urls import path
from .views import (
    HomeView,
    SignUpView,
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
    update_task_status,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tasks/new/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("tasks/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("tasks/<int:pk>/status/<str:status>/", update_task_status, name="task_status"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
