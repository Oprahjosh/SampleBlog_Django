from django.urls import path

from myBlog.views import IndexView

app_name = 'myBlog'

urlpatterns = [
    path ( '' ,IndexView , name='home' )
]
