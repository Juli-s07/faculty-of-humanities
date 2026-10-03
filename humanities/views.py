from django.shortcuts import render

from humanities.admin import FacultyInfoAdmin
from humanities.models import Program, Department, FacultyInfo


# Create your views here.
def index(request):
    info = FacultyInfo.objects.first()
    return render(request, 'humanities/home.html', {'info': info})
def show_all_programs(request):
def show_program(request, id):
def show_all_departments(request):
    departments = Department.objects.all()
    return render(request, 'humanities/department_list.html', {'departments': departments})
def show_department(request, id):
    department = Department.objects.get(id=id)
    return render(request, 'humanities/department_detail.html', {'department': department})
