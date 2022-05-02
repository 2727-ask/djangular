from django.db import models
# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=61)
    description = models.TextField(null=True)
    def __str__(self):
        return self.title