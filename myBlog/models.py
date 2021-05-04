from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


'''class Register1(models.Model):
    username1 = models.CharField(max_length=50)
    email = models.EmailField
    password = models.CharField(max_length=20)'''


def __str__(self):
    return self.title


'''def __str__(self):
    return self.username
'''
