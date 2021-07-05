from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome")
]
