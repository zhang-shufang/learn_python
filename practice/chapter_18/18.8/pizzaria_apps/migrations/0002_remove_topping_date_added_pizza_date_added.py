# Generated by Django 4.2.5 on 2023-09-23 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaria_apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='date_added',
        ),
        migrations.AddField(
            model_name='pizza',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]