# Generated by Django 2.0 on 2020-03-03 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
