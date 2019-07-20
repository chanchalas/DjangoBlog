"""simpleblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from .views import home, detail, create_post,edit_post, delete_post, collapse, modal, like_post

urlpatterns = [
    path('',home, name='home'),
    path('detail/<int:id>/',detail, name='detail'),
    path('detail/<int:id>/like/',like_post, name='like_post'),
    path('create/',create_post, name='create_post'),
    path('detail/<int:id>/edit/',edit_post, name='edit_post'),
    path('detail/<int:id>/delete/',delete_post, name='delete_post'),
    path('collapse/',collapse, name='collapse'),
    path('modal/',modal, name='modal'),
]
