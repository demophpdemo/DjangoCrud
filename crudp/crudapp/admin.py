from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Employeer)
class EmployeerAdmin(admin.ModelAdmin):
    list_display = ['ename']