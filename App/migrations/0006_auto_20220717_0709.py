# Generated by Django 3.1.12 on 2022-07-17 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_title',
            field=models.CharField(max_length=200),
        ),
    ]
