from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/dashboard.html')

def contact(request):
    return render(request, 'accounts/products.html')

def users(request):
    return render(request, 'accounts/customer.html')
# Create your views here.
