from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    head_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=100)
    coordinator_contact = models.TextField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')

    def __str__(self):
        return f"{self.name} ({self.department.name})"

class Discipline(models.Model):
    name = models.CharField(max_length=200)
    programs = models.ManyToManyField(Program, related_name="disciplines")

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.name

class FacultyInfo(models.Model):
    description = models.TextField()
    main_info = models.TextField()
    contacts = models.TextField()

    class Meta:
        verbose_name_plural = "Faculty Info"

    def __str__(self):
        return "Faculty Info"
