------ Project Setup ------
Please follow bellow steps to setup the project.

1. Create virtual environment
python -m venv venv

2. Activate the virtual env
.\venv\Scripts\activate

3. Install project dependencies
 pip install -r requirements.txt

4. Create django migrations
python manage.py makemigrations

5. Migrate the SQL changes
 python manage.py migrate

6. Create SuperUser
python manage.py createsuperuser 

7. Run the server
python manage.py runserver

Create Method:
    endpoints: 127.0.0.1:8000/api/employee/details/
    method: Post
    json data: 
        {
    "first_name": "Abhi",
    "last_name": "Dey",
    "workEmail": "dey.a@admin.com",
    "personalEmail": "",
    "mobile":"+919890262022",
    "gender": "Male",                           Choice: Male, Female, Other
    "bloodGroup": "A+",
    "dob": "1995-05-12",
    "maritalStatus": "Single",                   Choice: Single, Married, Divorced
    "profile_pic":"",
    "designation":"Software Developer",
    "department":"DE",
    "dateOfJoin":"2021-08-15"
    }

Get All details: 
    endpoints: 127.0.0.1:8000/api/employee/details/

Get particular details: 
    endpoints: 127.0.0.1:8000/api/employee/get-details/<str:pk>
    ex. 127.0.0.1:8000/api/employee/get-details/8

Update Employee details:
    endpoints: 127.0.0.1:8000/api/employee/details/<str:pk>
    ex. 127.0.0.1:8000/api/employee/details/7
        {
            "designation":"Python Developer"
        }
Delete Employee details: 
    endpoints: 127.0.0.1:8000/api/employee/details/<str:pk>
    ex. 127.0.0.1:8000/api/employee/details/6

Note: Please check postman collection using this link: 
https://documenter.getpostman.com/view/20290870/2s93CSnATS
