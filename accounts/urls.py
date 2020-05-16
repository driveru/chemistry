from django.urls import path
from . import views as account_views
from django.contrib.auth import views

urlpatterns = [
    path('signup', account_views.signup, name='signup' ),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]
