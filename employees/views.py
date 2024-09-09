from django.shortcuts import render
from .models import Department
from django.shortcuts import render, get_object_or_404
from .models import Employee


def department_tree(request):
    departments = Department.objects.all()
    return render(request, 'department_tree.html', {'departments': departments})


def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employee_detail.html', {'employee': employee})
