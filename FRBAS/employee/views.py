from django.shortcuts import render,redirect
from .script import  EmployeeScript
from decorators import is_loged_in,is_loged_out
#   Create your views here.
@is_loged_in
def employeeSignUp(request):
     employee = EmployeeScript()
     gender = employee.employeeGender()
     country = employee.employeeCountry()
     autority = employee.employeeAuthority()
     if request.method == "POST":
         request = employee.employeeSignup(request)
     return render(request,"employee/employeeSignup.html",{"gender":gender,"country":country,"autority":autority})

#   Employee Account Password Change
def employeeAccountPassword(request):
     employee = EmployeeScript()
     if request.method == "POST":
         request = employee.employeePassword(request)

#   Employee Sign-in
@is_loged_in
def employeeSignIn(request):
     success = False
     employee = EmployeeScript()
     if request.method == "POST":
         request,success = employee.employeeSignIn(request)
         if success:
             return redirect("employee:home")
     return render(request,"employee/employeeSignIn.html",{})
 
#   Employee Department
@is_loged_out
def employeeDepartment(request):
     employee = EmployeeScript()
     employeeDeparmentAll = employee.employeeModelAll("department")
     if request.method == "POST":
         request,employeeDeparmentAll = employee.employeeDepartment(request) 
     return render(request,"employee/employeeDepartment.html",{"employeeDeparmentAll":employeeDeparmentAll})

#   Employee Job
@is_loged_out
def employeeJob(request):
     employee = EmployeeScript()
     employeeJobAll = employee.employeeModelAll("job")
     employeeDeparmentAll = employee.employeeModelAll("department")
     if request.method == "POST":
         request,employeeJobAll = employee.employeeJob(request) 
     return render(request,"employee/employeeJob.html",{"employeeJobAll":employeeJobAll,"employeeDeparmentAll":employeeDeparmentAll})

#   Employee Job Assign
@is_loged_out
def employeeWork(request):
     employee = EmployeeScript()
     if request.method == "POST":
         request = employee.employeeWork(request) 
     return render(request,"employee/employeeJob.html",{})

#   Employee Change Password:
def employeePassword(request):
     employee = EmployeeScript()
     if request.method == "POST":
         request = employee.employeePassword(request) 
     return render(request,"employee/employeePassword.html",{})

#   Employee Home page
@is_loged_out
def employeeHome(request):
     if request.method == "POST":
         pass  
     return render(request,"employee/employeeHome.html",{})
