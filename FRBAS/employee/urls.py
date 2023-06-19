from django.urls import path
from .import views

app_name = 'employee'
urlpatterns = [
     path("",           views.employeeSignIn,    name="signIn"),
     path("signup/",    views.employeeSignUp,    name="signup"),
     path("home/",      views.employeeHome,      name="home"),
     path("department/",views.employeeDepartment,name="department"),
     path("job/",       views.employeeJob,       name="job"),
     path("password/",  views.employeePassword,  name="password"),
     path("work/",      views.employeeWork,      name="work"),
]