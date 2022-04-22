from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('posts.html', views.posts, name='posts'),
    path('projects.html', views.projects, name='projects'),
    path('base.html', views.base, name='base'),

]