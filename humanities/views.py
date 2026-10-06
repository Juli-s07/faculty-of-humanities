from django.shortcuts import render

from humanities.models import Department, ExchangeProgram, FacultyInfo, Program


# Create your views here.
def index(request):
    info = FacultyInfo.objects.first()
    return render(request, "humanities/home.html", {"info": info})


def show_all_programs(request):
    programs = Program.objects.all()
    return render(request, "humanities/program_list.html", {"programs": programs})


def show_program(request, id):
    program = Program.objects.get(id=id)
    return render(request, "humanities/program_detail.html", {"program": program})


def show_all_departments(request):
    departments = Department.objects.all()
    return render(
        request, "humanities/department_list.html", {"departments": departments}
    )


def show_department(request, id):
    department = Department.objects.get(id=id)
    return render(
        request, "humanities/department_detail.html", {"department": department}
    )


def show_exchange_programs(request):
    exchange_programs = ExchangeProgram.objects.all()
    return render(
        request,
        "humanities/exchange_programs.html",
        {"exchange_programs": exchange_programs},
    )
