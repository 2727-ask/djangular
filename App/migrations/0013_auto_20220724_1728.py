# Generated by Django 3.1.12 on 2022-07-24 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_auto_20220721_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profie_pic',
            new_name='profile_pic',
        ),
    ]