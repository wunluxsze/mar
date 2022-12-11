"""djangoTrails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from trail import views


urlpatterns = [
    path('posts/comments/<int:postId>/<int:countComments>/', views.comments, name='comments'),
    path('posts/likes/<int:postId>/<int:countLikes>/', views.likes, name='likes'),
    path('access/', views.access, name='access'),
    path('posts/popular/<int:countPosts>/', views.popular, name='posts'),
    path('posts/last/<int:countPosts>/', views.last, name='last posts'),
    path('posts/<int:countPosts>/', views.posts, name='posts'),
    path('user/', views.user, name='user'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('error/', views.error, name='error'),
    path('json/', views.json, name='json'),
    path('set/', views.set, name='set'),
    path('get/', views.get, name='get')
]
