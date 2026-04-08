from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import TaskForm
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by("-creat_at")


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_create.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")
    context_object_name = "task"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_create.html"
    success_url = reverse_lazy("task_list")
    context_object_name = "task"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
