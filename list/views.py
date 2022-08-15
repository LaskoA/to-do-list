from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import TaskForm
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    template_name = "list/task_list.html"


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to-do-list:task-list")
    template_name = "list/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to-do-list:task-list")
    template_name = "list/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to-do-list:task-list")
    template_name = "list/task_delete.html"


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    template_name = "list/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to-do-list:tag-list")
    template_name = "list/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to-do-list:tag-list")
    template_name = "list/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to-do-list:tag-list")
    template_name = "list/tag_delete.html"


def task_status_change(request, pk):
    task = Task.objects.get(id=pk)
    if task.done:
        task.done = False
    else:
        task.done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("to-do-list:task-list"))
