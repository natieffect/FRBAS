from .models import *
from django.contrib.auth.hashers import make_password, check_password
from frbasScript import  FrbasScript
from script.frbasScriptTime import FrbasScriptTimeDate
class EmployeeScript:
    def __init__(self) -> None:
         self.frbasScript = FrbasScript()
         self.timeDateValue  = FrbasScriptTimeDate()
#     Employee Sign Up 
    def employeeSignup(self,request):
        try:
             employee = Employee(
                                   email=request.POST.get("email"), 
                                   fname = request.POST.get("fname"),
                                   phone = request.POST.get("phone"),
                                   birth = request.POST.get("birth"),
                                   id = request.POST.get("id"),
                                   gender = request.POST.get("gender"),
                                   coutry = request.POST.get("country"))
             
             account = Account(user=employee,password=make_password(self.frbasScript.config.get("DEFAULT","PASSWORD")),autority=request.POST.get("autority"))
             employee.save()
             account.save()
             request = self.frbasScript.set_message("success","EMPLOYEE_SIGN_UP","SIGNUP_SUCCESS",request)
        except Exception as e: 
             print(e)
             request = self.frbasScript.set_message("error","EMPLOYEE_SIGN_UP","SIGNUP_ERROR",request)
        return request
   
#     Employee Gender 
    def employeeGender(self):
         gender = []
         for value in GENDER:
              gender.append({'value': value[0], 'name':value[1]})
         return gender
    
#     Employee CITY  
    def employeeCountry(self):
         country = []
         for value in CITY:
              country.append({'value': value[0], 'name':value[1]})
         return country

#     Employee SYSTEM_AUTHORITY  
    def employeeAuthority(self):
         autority = []
         for value in SYSTEM_AUTHORITY:
              autority.append({'value': value[0], 'name':value[1]})
         return autority

#    Employee Password Change
    def employeePassword(self,request):
         try:
              account = Account.object.get(user__email=self.frbasScript.sesstionValueGet('email',request))
              if request.POST['password'] == request.POST['conformpassword']:
                     account.password = make_password(request.POST['password'])
                     account.save()
                     request = self.frbasScript.set_message("success","EMPLOYEE_ACCOUNT","ACCOUNT_PASSWORD_SUCCESS",request)
              else:
                     request = self.frbasScript.set_message("warning","EMPLOYEE_ACCOUNT","ACCOUNT_PASSWORD_ERROR_ONE",request)
         except Exception as e:
               print(e)
               request = self.frbasScript.set_message("error","EMPLOYEE_ACCOUNT","ACCOUNT_PASSWORD_ERROR_TWO",request)
         return request

#    Employee Log in
    def employeeSignIn(self,request):
          success = False
          try:
              account = Account.objects.get(user__email=request.POST['email'])
              if check_password(request.POST['password'],account.password):
                   request,success = self.frbasScript.login_sesstion(account,request)
              else:
                   request = self.frbasScript.set_message("warning","EMPLOYEE_ACCOUNT","ACCOUNT_PASSWORD_ERROR_ONE",request)
          except Exception as e:
                request = self.frbasScript.set_message("error","EMPLOYEE_ACCOUNT","ACCOUNT_LOGIN_ERROR",request)
                print(e)
          return request,success

#    Employee Department
    def employeeDepartment(self,request):
         try:
              department  = Department(name    =request.POST.get('name'),
                                       detail  =request.POST.get('detail'),
                                       depid   =request.POST.get('depid'),
                                       creater =Employee.objects.get(email=self.frbasScript.sesstionValueGet('email',request)))
              department.save()
              request = self.frbasScript.set_message("success","EMPLOYEE_DEPARTMENT","DEPARTMENT_SUCCESS",request)
         except Exception as e:
              print(e)
              request = self.frbasScript.set_message("error","EMPLOYEE_DEPARTMENT","DEPARTMENT_ERROR",request)
              
         return request
              
#    Employee Job
    def employeeJob(self,request):
         try:
              job = Job(department =Department.objects.get(id=request.POST.get('department')),
                        title      =request.POST.get('title'),
                        detail     =request.POST.get('detail'),
                        jobid      =request.POST.get('jobid'),
                        creater    =Employee.objects.get(email=self.frbasScript.sesstionValueGet('email',request)))
              request = self.frbasScript.set_message("success","EMPLOYEE_JOB","JOB_SUCCESS",request)
              job.save()
         except Exception as e:
              print(e)
              request = self.frbasScript.set_message("error","EMPLOYEE_JOB","JOB_ERROR",request)
         return request

#    Employee Work Assign
    def employeeWork(self,request):        
         try:
              work = Work(employee =Employee.objects.get(email=request.POST.get('employee')),
                          job      =Job.objects.get(id=request.POST.get('job')),
                          begin    =self.timeDateValue.timeAjustValue(request.POST.get('begin')),
                          finish   =self.timeDateValue.timeAjustValue(request.POST.get('finish')),
                          assigned =Employee.objects.get(email=self.frbasScript.sesstionValueGet('email',request)))
              work.save()
              request = self.frbasScript.set_message("success","EMPLOYEE_WORK","WORK_SUCCESS",request)
         except Exception as e:
              print(e)
              request = self.frbasScript.set_message("error","EMPLOYEE_WORK","WORK_ERROR",request) 
         return request
              
#   Employee model value status activate deactivate
    def statusActivateDeactivate(self,request):
         if request.POST.get("model") == "employee":
                employee        = Employee.objects.get(email=request.POST.get("id"))
                employee.status = request.POST.get("status")
                employee.trash  = request.POST.get("trash")
         elif request.POST.get("model") == "account":
                account        = Account.objects.get(id=request.POST.get("id"))
                account.status = request.POST.get("status")
                account.trash  = request.POST.get("trash")
         elif request.POST.get("model") == "department":
                department        = Department.objects.get(id=request.POST.get("id"))
                department.status = request.POST.get("status")
                department.trash  = request.POST.get("trash")
         else:
                job        = Job.objects.get(id=request.POST.get("id"))
                job.status = request.POST.get("status")
                job.trash  = request.POST.get("trash")

# Employee model get all value
    def employeeModelAll(self,model):
         if model == "employee":
              return Employee.objects.all()
         if model == "account":
              return Account.objects.all()
         if model == "job":
              return Job.objects.all()
         if model == "department":
              return Department.objects.all()
         if model == "work":
              return Work.objects.all()

         
         