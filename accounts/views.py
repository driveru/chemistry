from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . import forms as my_forms
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = my_forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'registration/signup.html', {'form': form})
            
        return redirect('login')
    else:
        form = my_forms.SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
