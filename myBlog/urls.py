from django.urls import path
from myBlog import views

app_name = 'myBlog'

urlpatterns = [
    path ( '' , views.IndexView , name='home' ),
    path ('post_detail/', views.post_detail , name = 'post_detail')
]
