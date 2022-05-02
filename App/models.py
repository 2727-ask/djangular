from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=61)
    description = models.TextField(null=True)
    parent = models.ForeignKey('self',null=True,on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.title