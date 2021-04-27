from django.contrib import admin
from django.urls import path, include

app_name = 'myBlog'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
]