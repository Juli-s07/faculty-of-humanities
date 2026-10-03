from django.urls import path
from . import views

app_name = "humanities"

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.show_all_programs, name='all_programs'),
    path('programs/<int:id>/', views.show_program, name='program'),
    path('departments/', views.show_all_departments, name='all_departments'),
    path('departments/<int:id>/', views.show_department, name='department'),
]
