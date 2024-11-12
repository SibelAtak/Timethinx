# Generated by Django 4.0.3 on 2022-03-23 14:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Müşteri', 'verbose_name_plural': 'Müşteriler'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Proje', 'verbose_name_plural': 'Projeler'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Görev', 'verbose_name_plural': 'Görevler'},
        ),
        migrations.AlterModelOptions(
            name='tasklog',
            options={'verbose_name': 'Görev Günlüğü', 'verbose_name_plural': 'Görev Günlükleri'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Çalışan', 'verbose_name_plural': 'Çalışanlar'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='tasklog',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='tasklog',
            name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.customer', verbose_name='Müşteri'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.project', verbose_name='Proje'),
        ),
        migrations.AddField(
            model_name='tasklog',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.task', verbose_name='Görev'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(max_length=50, verbose_name='Müşteri Adı'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=50, verbose_name='Proje Adı'),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(max_length=30, verbose_name='Görev Adı'),
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.user', verbose_name='Çalışan'),
        ),
        migrations.AlterField(
            model_name='tasklog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Başlangıç Tarihi'),
        ),
        migrations.AlterField(
            model_name='tasklog',
            name='hours_worked',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Çalışılan saat'),
        ),
        migrations.AlterField(
            model_name='tasklog',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Çalışan Adı'),
        ),
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Pozisyon'),
        ),
        migrations.AddConstraint(
            model_name='tasklog',
            constraint=models.CheckConstraint(check=models.Q(('hours_worked__gte', 0)), name='task_log_hours_worked_range'),
        ),
    ]
