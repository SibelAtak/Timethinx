# Generated by Django 3.2.9 on 2022-04-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklog',
            name='created_at',
            field=models.DateField(null=True, verbose_name='Başlangıç Tarihi'),
        ),
    ]
