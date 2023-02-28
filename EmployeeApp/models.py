from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from EmployeeApp.choices import GENDER_CHOICES, Marital_CHOICES
import random

# Create Employee models.
class Employee(models.Model):
    employeeNo = models.CharField("Employee No.", max_length=25, unique=True, editable=False, blank=False, null=False)
    first_name = models.CharField("First Name", max_length=50, blank=False, null=False)
    last_name = models.CharField("Last Name", max_length=50, blank=False, null=False)
    workEmail = models.EmailField("Work Email", max_length=100, unique=True, blank=False, null=False)
    personalEmail = models.EmailField("Personal Email", max_length=100, blank=True, null=True)
    mobile = PhoneNumberField('Mobile Phone', max_length=15, blank=False, null=False, unique=True)
    gender = models.CharField("Gender", max_length=10, choices=GENDER_CHOICES, blank=False, null=False)
    bloodGroup = models.CharField("Blood Group", max_length=10, blank=True, null=True)
    dob = models.DateField("Date of Birth")
    maritalStatus = models.CharField("Marital Status", max_length=10, choices=Marital_CHOICES, null=True, blank=True)
    profile_pic = models.ImageField("Profile Picture", upload_to ='static/ProfilePicture/', blank=True, null=True)
    designation = models.CharField("Designation", max_length=100, blank=False, null=False)
    department = models.CharField("Department", max_length=100, blank=True, null=True)
    dateOfJoin = models.DateField("Joining Date")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
    
    class Meta:
        verbose_name_plural = 'Employee Details'
        

    def save(self, *args, **kwargs):
        if not self.employeeNo:
            self.employeeNo = self.emp_no_generator()
            while Employee.objects.filter(employeeNo=self.employeeNo).exists():
                self.employeeNo = self.emp_no_generator()

        
        super(Employee, self).save(*args, **kwargs)

    def emp_no_generator(self):
        return "EMP"+str(random.randint(20012345, 90012345))

