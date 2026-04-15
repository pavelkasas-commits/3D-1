from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views.decorators.http import require_POST

from .forms import SignUpForm
from .forms import TaskForm
from .models import Task















class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")




class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.select_related("user").order_by("-creat_at")
        return Task.objects.filter(user=self.request.user).select_related("user").order_by("-creat_at")


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_create.html"
    success_url = reverse_lazy("task_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        if not self.request.user.is_superuser or not form.cleaned_data.get("user"):
            form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.select_related("user")
        return Task.objects.filter(user=self.request.user).select_related("user")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")
    context_object_name = "task"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.select_related("user")
        return Task.objects.filter(user=self.request.user).select_related("user")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_create.html"
    success_url = reverse_lazy("task_list")
    context_object_name = "task"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.select_related("user")
        return Task.objects.filter(user=self.request.user).select_related("user")



@login_required
@require_POST
def update_task_status(request, pk, status):
    if request.user.is_superuser:
        task = get_object_or_404(Task, pk=pk)
    else:
        task = get_object_or_404(Task, pk=pk, user=request.user)
    valid_statuses = {choice[0] for choice in Task.STATUS_CHOICES}

    if status not in valid_statuses:
        return HttpResponseBadRequest("Error")

    task.status = status
    task.save(update_fields=["status"])
    return redirect("task_list")
