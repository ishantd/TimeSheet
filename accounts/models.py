from django.db import models
from django.core.validators import int_list_validator
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    designation_name = (('Office Boy', 'Office Boy'),('Driver', 'Driver'),('Draftman', 'Draftman'),('Assistant', 'Assistant'),
    ('Sr Assistant', 'Sr Assistant'),('Secreatary', 'Secreatary'),('Executive', 'Executive'),('Sr Executive', 'Sr Executive'),
    ('Engineer', 'Engineer'),('Graduate Trainee', 'Graduate Trainee'),('GTE', 'GTE'),('Lead Engineer', 'Lead Engineer'),
    ('Sr Engineer', 'Sr Engineer'),('Manager', 'Manager'),('Assistant Manager', 'Assistant Manager'),
    ('Deputy Manager', 'Deputy Manager'),('Sr Manager', 'Sr Manager'),('Chief Manager', 'Chief Manager'),
    ('General Manager', 'General Manager'),('AVP', 'AVP'),('VP', 'VP'),('DP', 'DP'),('CEO', 'CEO'),('CMD', 'CMD'))  
    designation = models.CharField(max_length=200, null=True, choices=designation_name)
    location = models.CharField(max_length=200, null=True, choices=(('Delhi', 'Delhi'), ('Offshore', 'Offshore')))
    department_info = models.ForeignKey('DepInfo', on_delete=models.CASCADE, null=True, blank=True)
    service_type = models.CharField(max_length=200, null=True, choices=(('Regular', 'Regular'), ('Contract', 'Contract')))
    extended_hours = models.BooleanField(null=False, default=False)
    def __str__(self):
        return str(self.employee_id) + '-' + self.name
 
    
class Project(models.Model):
    type_level = (('OH', 'OH'), ('PA', 'PA'))
    project_type = models.CharField(max_length = 200, null = True, choices=type_level)
    project_id = models.IntegerField(primary_key=True)
    project_client = models.CharField(max_length = 200, null = True)
    name = models.CharField(max_length=200, null=True)
    date_created =  models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(null=True)
    start_date = models.DateTimeField(null=True)
    controlled_manhours = models.IntegerField(null=True)
    completion_date = models.DateTimeField(null=True)
    project_manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department_assigned = models.BooleanField(null=False, default=False)
    active = models.BooleanField(null=False, default=True)
    finished = models.BooleanField(null=False, default=False)
    def __str__(self):
        return str(self.project_id)

class Department(models.Model):
    department_name = models.ForeignKey('DepInfo', on_delete=models.CASCADE, null=True)
    project_assigned = models.ForeignKey(Project, on_delete=models.CASCADE)
    time_allocated = models.IntegerField(null=True)
    time_left = models.IntegerField(null=True)
    assigned_to = models.ManyToManyField(Employee)
    emp_assigned = models.BooleanField(null=False, default=False)
    active = models.BooleanField(null=False, default=True)
    def __str__(self):
        return (str(self.department_name) + " - "+str(self.project_assigned))
    # department = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)

class Report(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    everyday_hours = models.CharField(validators=[int_list_validator], max_length=100, null=True)
    hours_reported = models.IntegerField(null=True)
    week = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    extended_hours = models.BooleanField(default=False, null=False)
    complete = models.BooleanField(null=False, default=False)
    approved = models.BooleanField(default=False, null=False)
    rejected = models.BooleanField(default=False, null=False)
    def __str__(self):
        return (str(self.employee.name) + " - "+str(self.project.name)+ " - "+str(self.hours_reported) + " Hours")

class DepInfo(models.Model):
    department_level = (('Corporate', 'Corporate'),('Finance', 'Finance'),('Business Development', 'Business Development'),
    ('Human Resource', 'Human Resource'),('Library', 'Library'),('Document Control', 'Document Control'),
    ('Information Technology', 'Information Technology'),('Planning', 'Planning'),('Administration', 'Administration'),
    ('Process', 'Process'),('Quality', 'Quality'),('Mechanical', 'Mechanical'),('Projects', 'Projects'),('Instrumentation', 'Instrumentation'),
    ('Civil Structural', 'Civil Structural'),('Procurement', 'Procurement'),('Electrical', 'Electrical'),('Piping', 'Piping'))
    department_name = models.CharField(max_length = 200, null = True, choices=department_level)
    department_hod = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return (str(self.department_name))

class Activity(models.Model):
    name = models.ForeignKey('Act', on_delete=models.CASCADE, null=True, blank=True)
    department_info = models.ForeignKey(DepInfo, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return (str(self.name) + str(self.department_info))

class Report_extended(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    everyday_hours = models.CharField(validators=[int_list_validator], max_length=100, null=True)
    hours_reported = models.IntegerField(null=True)
    week = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    approved = models.BooleanField(default=False,null=False)
    complete = models.BooleanField(null=False, default=False)
    rejected = models.BooleanField(default=False, null=False)
    def __str__(self):
        return (str(self.employee.name) + " - "+str(self.project.name)+ " - "+str(self.hours_reported) + " Hours")

class Act(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.name)
    
