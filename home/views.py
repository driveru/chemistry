from django.shortcuts import render
from django.http import HttpResponse
from knowledge.views import is_allowed
# Create your views here.
def index(request):
    context = {}
    if is_allowed(request.user.groups.all()):
        context = {'allowed': True}
    return render(request, 'home/index.html')

def about(request):
    context = {}
    if is_allowed(request.user.groups.all()):
        context = {'allowed': True}
    return render(request, 'home/about.html', context)
