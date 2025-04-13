from django.shortcuts import render
from app1.models import Employee
# Create your views here.


def fetch_data(request):
    data = Employee.objects.all()
    return render(request, 'test.html', {'data': data})


def hello(request):
    return render(request, 'index.html')
