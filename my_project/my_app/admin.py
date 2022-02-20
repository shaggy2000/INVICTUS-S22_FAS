from django.contrib import admin

# Register your models here.

from .models import UserInfo, Entry

admin.site.register(UserInfo)
admin.site.register(Entry)
