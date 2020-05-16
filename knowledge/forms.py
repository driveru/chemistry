import django_filters
from . import models
from django.forms import ModelForm

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = models.Task
        fields = ['level', 'title', 'id']

class TaskForm(ModelForm):
    class Meta:
        model = models.Task
        fields = ('title', 'content_1', 'content_2', 'level')

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    for field in self.fields:
    #        self.fields[field].widget.attrs['class']
