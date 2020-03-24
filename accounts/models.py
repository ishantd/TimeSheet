from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    department_level = (('Process', 'Process'), ('Structure', 'Structure'), ('Piping', 'Piping'), ('Instrumentation', 'Instrumentation'), 
                        ('Electrical', 'Electrical'), ('Projects', 'Projects'), ('Mechanical', 'Mechanical'), ('Quality', 'Quality'), ('Documentation', 'Documentation'))
    department_name = models.CharField(max_length = 200, null = True, choices=department_level)
    # tasks_assignted = models.ForeignKey(Tasks_Assignment, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name
    
class Project(models.Model):
    type_level = (('OH', 'OH'), ('PA', 'PA'))
    project_type = models.CharField(max_length = 200, null = True, choices=type_level)
    project_id = models.IntegerField(null=True)
    priority_level = (('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low'))
    name = models.CharField(max_length=200, null=True)
    date_created =  models.DateTimeField(auto_now_add=True, null=True)
    time_assigned = models.IntegerField(null=True)
    due_date = models.DateTimeField(null=True)
    priority = models.CharField(max_length = 200, null = True, choices=priority_level)
    project_manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name +  " - " + str(self.project_id))

class Department(models.Model):
    department_level = (('Process', 'Process'), ('Structure', 'Structure'), ('Piping', 'Piping'), ('Instrumentation', 'Instrumentation'), 
                        ('Electrical', 'Electrical'), ('Projects', 'Projects'), ('Mechanical', 'Mechanical'), ('Quality', 'Quality'), ('Documentation', 'Documentation'))
    department_name = models.CharField(max_length = 200, null = True, choices=department_level)
    project_assigned = models.ForeignKey(Project, on_delete=models.CASCADE)
    manager_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    time_allocated = models.IntegerField(null=True)
    time_left = models.IntegerField(null=True)
    def __str__(self):
        return (str(self.manager_name) + " - "+str(self.project_assigned))
    # department = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)

class Report(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    activity = models.CharField(max_length=200, null=True)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True)
    hours_reported = models.IntegerField(null=True)
    def __str__(self):
        return (str(self.employee.name) + " - "+str(self.project.name)+ " - "+str(self.hours_reported) + " Hours")
