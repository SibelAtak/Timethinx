# Generated by Django 4.0.3 on 2022-03-23 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_task_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
