from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    employee_id = forms.IntegerField()
    name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    manager = forms.ModelChoiceField(queryset=Employee.objects.all())
    department_name = forms.ChoiceField(choices=(('Process', 'Process'), ('Structure', 'Structure'), ('Piping', 'Piping'), ('Instrumentation', 'Instrumentation'), 
                        ('Electrical', 'Electrical'), ('Projects', 'Projects'), ('Mechanical', 'Mechanical'), ('Quality', 'Quality'), ('Documentation', 'Documentation'), ('Planning', 'Planning')))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'employee_id', 'name', 'email'
                  , 'phone', 'manager', 'department_name')
        
class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        
class ProjectForm(ModelForm):
    
    class Meta:
        model = Project
        fields = '__all__'
        