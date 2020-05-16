from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
# Create your views here.

def index(request):
    tasks = models.Task.objects.all()
    filter = forms.TaskFilter(request.GET, queryset=tasks)
    form = forms.TaskForm()
    context = {'tasks': tasks, 'filter': filter, 'form': form}
    if is_allowed(request.user.groups.all()):
        context['allowed'] = True
    return render(request, 'knowledge/index.html', context)


class CustomSuccessMessageMixin:
    success_message = ''

    def get_success_message(self):
        task = self.get_object()
        success_message = self.success_message.replace('$^&!@', f'№{ task.id }')
        return success_message

    def form_valid(self, form):
        success_message = self.get_success_message()
        messages.success(self.request, success_message)
        return super().form_valid(form)


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'knowledge/create.html'
    form_class = forms.TaskForm
    model = models.Task
    success_url = reverse_lazy('knowledge_index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not is_allowed(self.request.user.groups.all()):
            return self.handle_no_permission()
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        title = self.request.POST['title']
        success_message = f'Новая { title } добавлена!'
        messages.success(self.request, success_message)
        return super().form_valid(form)

class EditTaskView(CustomSuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = models.Task
    template_name = 'knowledge/create.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy('knowledge_index')
    success_message = 'Задание $^&!@ отредактировано!'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not is_allowed(self.request.user.groups.all()):
            return self.handle_no_permission()
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['edit'] = True
        if is_allowed(self.request.user.groups.all()):
            kwargs['allowed'] = True
        return super().get_context_data(**kwargs)


class DeleteTaskView(CustomSuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = models.Task
    template_name = 'knowledge/create.html'
    success_url = reverse_lazy('knowledge_index')
    success_message = 'Задание $^&!@ удалено!'


    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect('knowledge_index')

    def post(self, request, *args, **kwargs):
        if not is_allowed(self.request.user.groups.all()):
            return self.handle_no_permission()
        success_message = self.get_success_message()
        messages.success(self.request, success_message)
        return super().post(request)

def is_allowed(user_groups):
    print(user_groups)
    allowed_groups = set(['admin', 'moder'])
    groups = [x.name for x in user_groups]
    if allowed_groups.intersection(set(groups)):
        return True
    return False
