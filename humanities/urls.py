from django.urls import path
from . import views

app_name = "humanities"

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.all_programs, name='all_programs'),
    path('programs/<int:id>/', views.program, name='program'),
    path('departments/', views.all_departments, name='all_departments'),
    path('departments/<int:id>/', views.department, name='department'),
]
