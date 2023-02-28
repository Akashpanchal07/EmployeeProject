from django.urls import path
from EmployeeApp import views


app_name = 'EmployeeApp'

urlpatterns = [

    # Employee Endpoints
    # get all employee details and Create Employee details[Get, Post]
    path("employee/details/", views.EmployeeAPIView.as_view()),

    # Delete and Update employee details by id
    path("employee/details/<str:pk>", views.EmployeeAPIView.as_view()),

    # Get particular employee Details by id
    path("employee/get-details/<str:pk>", views.OneEmployeeDetailsApiView.as_view())
    
]




""" Postman Collection link
https://documenter.getpostman.com/view/20290870/2s93CSnATS
"""