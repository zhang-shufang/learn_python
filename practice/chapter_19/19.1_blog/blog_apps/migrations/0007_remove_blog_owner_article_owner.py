# Generated by Django 4.2.5 on 2023-09-29 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_apps', '0006_blog_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='owner',
        ),
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
