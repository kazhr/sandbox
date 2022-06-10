from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import Task, TodoList


class TodoListAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {"widget": CheckboxSelectMultiple},
    }


# Register your models here.
admin.site.register(Task)
admin.site.register(TodoList, TodoListAdmin)
