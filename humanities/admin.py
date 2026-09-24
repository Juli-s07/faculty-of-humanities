from django.contrib import admin

# Register your models here.
from .models import Department, Program, Discipline, Teacher, FacultyInfo

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Discipline)
admin.site.register(Teacher)
admin.site.register(FacultyInfo)
