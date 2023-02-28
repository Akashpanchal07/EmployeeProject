from django.contrib import admin
from EmployeeApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", 
                    "employeeNo", 
                    "first_name", 
                    "last_name", 
                    "workEmail",
                    "mobile", 
                    "designation", 
                    "department", 
                    "dateOfJoin", 
                    "created_at"]
    search_fields = ('employeeNo', 'designation', 'department')
admin.site.register(Employee, EmployeeAdmin)