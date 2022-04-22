from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts, name='posts'),
    path('projects/', views.projects, name='projects'),
    path('base/', views.base, name='base'),

]