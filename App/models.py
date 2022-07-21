from email.policy import default
from operator import mod
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=61)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False, null=True)
    profie_pic = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=60, null=True,blank=True)
    bio = models.TextField(null=True, blank=True)
    github = models.TextField(null=True, blank=True)
    social = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=200, blank=True, default="Untitled")
    blog_desc = models.TextField()
    content = models.TextField()
    date_published = models.DateTimeField(null=True)

    def __str__(self):
        return self.blog_title
