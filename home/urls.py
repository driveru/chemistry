from django.urls import path
from . import views as home_views

urlpatterns = [
    path('', home_views.index, name='home_index'),
    path('about', home_views.about, name='about')
]
