from django.urls import path
from .views import IndexView

app_name = 'myBlog'

urlpatterns = [
    path('', IndexView, name='home'),
]
