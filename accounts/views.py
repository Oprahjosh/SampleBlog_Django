from django.shortcuts import render

'''from .models import Post
from django.views.generic import ListView'''


# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')
