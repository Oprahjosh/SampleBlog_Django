# from django.shortcuts import render
from myBlog.models import Post
from django.views.generic import ListView

# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = 'myBlog/home.html'
    context_object_name = 'home'
