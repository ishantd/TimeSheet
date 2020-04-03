from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('accounts/', views.contact),
    path('timesheet/<str:emp_id>/', views.timesheet),
    path('create/', views.create),
    path('create_employee/', views.createEmployee, name="create_employee"),
    path('view_employees/', views.viewEmployees, name='view_employees'),
    path('update_employee/<str:pk>/', views.updateEmployee, name='update_employee'),
    path('timesheetEntry/', views.timesheetEntry),
]