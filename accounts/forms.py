from django.forms import ModelForm
from .models import *

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        