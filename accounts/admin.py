from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Employee)
admin.site.register(Tasks)
admin.site.register(Tasks_Assignment)
admin.site.register(employeeTasks)
