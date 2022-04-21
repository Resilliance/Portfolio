from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'blogs/home.html')

def about(request):
    return render(request,'blogs/about.html')

def projects(request):
    return render(request,'blogs/projects.html')

def posts(request):
    return render(request,'blogs/posts.html')