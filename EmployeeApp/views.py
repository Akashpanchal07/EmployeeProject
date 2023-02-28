from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from EmployeeApp.models import Employee
from EmployeeApp.serializers import EmployeeSerializer
from django.http import Http404

# Create EmployeeAPIView.
class EmployeeAPIView(APIView):

    # Get All data.
    def get(self, request):
        
        """ Get All Employee Details """
        try:
            employeeObj = Employee.objects.all()
            jsonData = EmployeeSerializer(employeeObj, many = True)
            employeeData = jsonData.data
            return Response({
                "status": "success",
                "message":"All Employee Details fetched successfully",
                "data":employeeData
                }, status=200)
        except Employee.DoesNotExist:
            return Response({
                "status": "warning", 
                "message":"You don't have any Employee details", 
                "data":[]}, status=200)
    
    # Create Method.
    def post(self, request, *args, **kwargs):
        """ Create Employee Details """

        first_name = request.data.get('first_name', "")
        last_name = request.data.get('last_name', "")
        workEmail = request.data.get('workEmail', "")
        personalEmail = request.data.get('personalEmail', "")
        mobile = request.data.get('mobile', "")
        gender = request.data.get('gender', "")
        bloodGroup = request.data.get('bloodGroup', "")
        dob = request.data.get('dob', "")
        maritalStatus = request.data.get('maritalStatus', "")
        profile_pic = request.data.get('profile_pic', "")
        designation = request.data.get('designation', "")
        department = request.data.get('department', "")
        dateOfJoin = request.data.get('dateOfJoin', "")

        try:
            createEmployeeDetails = Employee.objects.create(
                                                            first_name=first_name,
                                                            last_name=last_name,
                                                            workEmail=workEmail,
                                                            personalEmail=personalEmail,
                                                            mobile=mobile,
                                                            gender=gender,
                                                            bloodGroup=bloodGroup,
                                                            dob=dob,
                                                            maritalStatus=maritalStatus,
                                                            profile_pic=profile_pic,
                                                            designation=designation,
                                                            department=department,
                                                            dateOfJoin=dateOfJoin
                                                        )
            createEmployeeDetails.save()
            responseData = {
            "status": "success",
            "message": "Employee Details is Successfully Created!!"}
            return Response(responseData, status=status.HTTP_200_OK)
        except:
            responseData = {
            "status": "warning",
            "message": "Something went to wrong!!!"}
            return Response(responseData, status=status.HTTP_200_OK)
        

    # Update Method. (Partial Update)
    def put(self, request, pk=None, format=None):  
        employeeObj = Employee.objects.get(pk=pk)  
        serializer = EmployeeSerializer(data=request.data, partial=True ,instance = employeeObj)  
        if serializer.is_valid(raise_exception=True):  
            serializer.save()  
            return Response({
                "status": "success",
                "message": "Employee Details updated Successfully!!!",
                "data": serializer.data

            }, status=status.HTTP_200_OK) 
        else:
            return Response({
                "status": "warning",
                "message": "Something went to wrong!!!",

            }, status=status.HTTP_200_OK)
    
    # Delete Method.
    def delete(self, request, pk=None, format=None):
        empObj = Employee.objects.get(pk=pk)
        print(empObj.id)

        empObj.delete()
        return Response({
            "status": "success",
            "msg": "Employee Details Deleted Successfully!!!"},
            status=status.HTTP_200_OK)


# Get Partcular Employee details by id
class OneEmployeeDetailsApiView(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Employee.objects.all()
        serializer = EmployeeSerializer(data, many=False)
        return Response(serializer.data) 

