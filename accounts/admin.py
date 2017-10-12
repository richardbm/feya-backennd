from django.contrib import admin
from accounts import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Membership)