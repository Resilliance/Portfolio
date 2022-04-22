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

def base(request):
    return render(request,'blogs/base.html')

def recycpal(request):
    return render(request, 'blogs/projects/recycpal.html')

def pharmeasy(request):
    return render(request, 'blogs/projects/pharmeasy.html')

def valleyball(request):
    return render(request, 'blogs/projects/valleyball.html')

def mycelium(request):
    return render(request, 'blogs/projects/mycelium.html')

def enterreality(request):
    return render(request, 'blogs/projects/enterreality.html')

def soildrencher(request):
    return render(request, 'blogs/projects/soildr.html')