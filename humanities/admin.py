from django.contrib import admin

# Register your models here.
from .models import (
    Department,
    Discipline,
    ExchangeProgram,
    FacultyInfo,
    Program,
    Teacher,
)

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Discipline)
admin.site.register(Teacher)
admin.site.register(ExchangeProgram)


@admin.register(FacultyInfo)
class FacultyInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()
