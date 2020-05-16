from django.urls import path
from . import views as knowledge_views

urlpatterns = [
    path('', knowledge_views.index, name='knowledge_index'),
    path('create', knowledge_views.CreateTaskView.as_view(), name='create_task'),
    path('edit/<int:pk>', knowledge_views.EditTaskView.as_view(), name='edit_task'),
    path('delete/<int:pk>', knowledge_views.DeleteTaskView.as_view(), name='delete_task'),
]
