from django.db import models
from django.core.validators import int_list_validator
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(null=True)
    department_level = (('Process', 'Process'), ('Structure', 'Structure'), ('Piping', 'Piping'), ('Instrumentation', 'Instrumentation'), 
                        ('Electrical', 'Electrical'), ('Projects', 'Projects'), ('Mechanical', 'Mechanical'), ('Quality', 'Quality'), ('Documentation', 'Documentation'), ('Planning', 'Planning'))
    department_name = models.CharField(max_length = 200, null = True, choices=department_level)
    def __str__(self):
        return str(self.employee_id)
    
class Project(models.Model):
    type_level = (('OH', 'OH'), ('PA', 'PA'))
    project_type = models.CharField(max_length = 200, null = True, choices=type_level)
    project_id = models.IntegerField(primary_key=True)
    priority_level = (('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low'))
    name = models.CharField(max_length=200, null=True)
    date_created =  models.DateTimeField(auto_now_add=True, null=True)
    time_assigned = models.IntegerField(null=True)
    due_date = models.DateTimeField(null=True)
    priority = models.CharField(max_length = 200, null = True, choices=priority_level)
    project_manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department_assigned = models.BooleanField(null=False, default=False)
    def __str__(self):
        return str(self.project_id)

class Department(models.Model):
    department_level = (('Process', 'Process'), ('Structure', 'Structure'), ('Piping', 'Piping'), ('Instrumentation', 'Instrumentation'), 
                        ('Electrical', 'Electrical'), ('Projects', 'Projects'), ('Mechanical', 'Mechanical'), ('Quality', 'Quality'), ('Documentation', 'Documentation'),('Planning', 'Planning'))
    department_name = models.CharField(max_length = 200, null = True, choices=department_level)
    project_assigned = models.ForeignKey(Project, on_delete=models.CASCADE)
    time_allocated = models.IntegerField(null=True)
    time_left = models.IntegerField(null=True)
    def __str__(self):
        return (str(self.department_name) + " - "+str(self.project_assigned))
    # department = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)

class Report(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    activity = models.CharField(max_length=200, null=True)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    everyday_hours = models.CharField(validators=[int_list_validator], max_length=100, null=True)
    hours_reported = models.IntegerField(null=True)
    week = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    def __str__(self):
        return (str(self.employee.name) + " - "+str(self.project.name)+ " - "+str(self.hours_reported) + " Hours")

 
    
