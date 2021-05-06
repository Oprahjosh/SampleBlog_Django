from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name= 'comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add= True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body,self.name)