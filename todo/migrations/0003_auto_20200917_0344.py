# Generated by Django 3.1.1 on 2020-09-16 22:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200917_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='complete',
        ),
        migrations.AddField(
            model_name='todo',
            name='details',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]