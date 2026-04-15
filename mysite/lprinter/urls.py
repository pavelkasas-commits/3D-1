from django.urls import path
from .views import (
    SignUpView,
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
    update_task_status,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("new/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("<int:pk>/status/<str:status>/", update_task_status, name="task_status"),
    path("signup/", SignUpView.as_view(), name="signup"),

]
