from django.shortcuts import render,redirect
from .script import  EmployeeScript
from decorators import is_loged_in,is_loged_out
# Create your views here.
@is_loged_out
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
     if request.method == "POST":
         request = employee.employeePassword(request)

# Employee Sign-in
@is_loged_out
def employeeSignIn(request):
     success = False
     employee = EmployeeScript()
     if request.method == "POST":
         request,success = employee.employeeSignIn(request)
         if success:
             return redirect("employee:home")
     return render(request,"employee/employeeSignIn.html",{})
 
#   Employee Log-In
@is_loged_in
def employeeHome(request):
     if request.method == "POST":
         pass  
     return render(request,"employee/employeeHome.html",{})
