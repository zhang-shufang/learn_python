from curses import tparm
from django.contrib import admin

# Register your models here.
from .models import Topic       # 句点可让 Django 在所在目录中查找。
from .models import Entry

admin.site.register(Topic)
admin.site.register(Entry)