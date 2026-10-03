from django.contrib import admin
from django.apps import apps

# Register your models here.
from .models import Department, Program, Discipline, Teacher, FacultyInfo

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Discipline)
admin.site.register(Teacher)

FacultyInfo = apps.get_model("humanities", "FacultyInfo")
@admin.register(FacultyInfo)
class FacultyInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()
