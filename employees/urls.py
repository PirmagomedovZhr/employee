from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.department_tree, name='department_tree'),
    path('employee/<int:id>/', views.employee_detail, name='employee_detail'),
]
