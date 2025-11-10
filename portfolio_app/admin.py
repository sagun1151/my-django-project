from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Portfolio
from .models import Project

admin.site.register(Student)
admin.site.register(Portfolio)
admin.site.register(Project)