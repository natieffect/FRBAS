from django.shortcuts import render,redirect
from .script import  EmployeeScript
from decorators import is_loged_in,is_loged_out
#   Create your views here.
@is_loged_in
def employeeSignUp(request):
     employee = EmployeeScript()
     if request.method == "POST":
         request = employee.employeeSignup(request)
     context = {"gender":employee.employeeGender(),
                "country":employee.employeeCountry(),
                "autority":employee.employeeAuthority()}
     return render(request,"employee/employeeSignup.html",context)

#   Employee Account Password Change
def employeeAccountPassword(request):
     employee = EmployeeScript()
     if request.method == "POST":
         request = employee.employeePassword(request)

#   Employee Sign-in
@is_loged_in
def employeeSignIn(request):    
     employee = EmployeeScript()
     if request.method == "POST":
         success = False
         request,success = employee.employeeSignIn(request)
         if success:
             return redirect("employee:home")
     return render(request,"employee/employeeSignIn.html",{})
 
#   Employee Department
@is_loged_out
def employeeDepartment(request):
     employee = EmployeeScript()
     if request.method == "POST":
         request = employee.employeeDepartment(request) 
     context = {"employeeDeparmentAll":employee.employeeModelAll("department")}
     return render(request,"employee/employeeDepartment.html",context)

#   Employee Job
@is_loged_out
def employeeJob(request):
     employee = EmployeeScript()
     if request.method == "POST":
         request = employee.employeeJob(request) 
     context = {"employeeJobAll":employee.employeeModelAll("job"),
                "employeeDeparmentAll":employee.employeeModelAll("department")}
     return render(request,"employee/employeeJob.html",context)

#   Employee Job Assign
@is_loged_out
def employeeWork(request):
     employee = EmployeeScript()
     if request.method == "POST":
         request = employee.employeeWork(request) 
     context = {"employeeAll":employee.employeeModelAll("employee"),
                "employeeJobAll":employee.employeeModelAll("job"),
                "employeeWorkAll":employee.employeeModelAll("work")}
     return render(request,"employee/employeeWork.html",context)

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
