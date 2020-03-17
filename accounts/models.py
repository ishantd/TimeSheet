from django.db import models

# Create your models here.
# if __name__ == "__main__":
#     main()
class Employee(models.Model):
    employee_id = models.IntegerField(null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    department_level = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    department = models.CharField(max_length = 200, null = True, choices=department_level)
    # tasks_assignted = models.ForeignKey(Tasks_Assignment, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name
    
class Tasks(models.Model):
    priority_level = (('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low'))
    name = models.CharField(max_length=200, null=True)
    date_created =  models.DateTimeField(auto_now_add=True, null=True)
    time_assigned = models.IntegerField(null=True)
    due_date = models.DateTimeField(null=True)
    priority = models.CharField(max_length = 200, null = True, choices=priority_level)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Tasks_Assignment(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(Employee)
    def __str__(self):
        return self.task
    # department = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    
class employeeTasks(models.Model):
    # task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    employee_task = models.ManyToManyField(Tasks_Assignment)