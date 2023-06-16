from django.shortcuts import render
from .script import  EmployeeScript
# Create your views here.
def employeeSignUp(request):
     employee = EmployeeScript()
     gender = employee.employeeGender()
     country = employee.employeeCountry()
     autority = employee.employeeAuthority()
     if request.method == "POST":
         request = employee.employeeSignup(request)
     return render(request,"employee/employeeSignup.html",{"gender":gender,"country":country,"autority":autority})

# Employee Account Password Change
def employeeAccountPassword(request):
     employee = EmployeeScript()
     pass