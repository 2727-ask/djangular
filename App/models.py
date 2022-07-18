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
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profie_pic = models.ImageField(null=True)
    def __str__(self):
        return self.user.email
        







class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)   
    blog_title = models.CharField(max_length=200)
    blog_desc = models.TextField()
    content = models.TextField()
    date_published = models.DateTimeField(null=True)


    
    def __str__(self):
        return self.blog_title    