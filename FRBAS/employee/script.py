from .models import Employee,GENDER,CITY,SYSTEM_AUTHORITY,Account
from django.contrib.auth.hashers import make_password, check_password
from frbasScript import  FrbasScript


class EmployeeScript:
    def __init__(self) -> None:
         self.mainscript = FrbasScript()
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
             
             account = Account(user=employee,password=make_password(self.mainscript.config.get("DEFAULT","PASSWORD")),autority=request.POST.get("autority"))
             employee.save()
             account.save()
             request = self.mainscript.set_message("success","EMPLOYEE_SIGN_UP","SIGNUP_SUCCESS",request)
        except Exception as e: 
             print(e)
             request = self.mainscript.set_message("error","EMPLOYEE_SIGN_UP","SIGNUP_ERROR",request)
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
              account = Account.object.get(user__email=request.session.get('user_email',False))
              if request.POST['password'] == request.POST['conformpassword']:
                     account.password = make_password(request.POST['password'])
                     account.save()
                     request = self.mainscript.set_message("success","EMPLOYEE_ACCOUNT","ACCOUNT_PASSWORD_SUCCESS",request)
              else:
                     request = self.mainscript.set_message("warning","EMPLOYEE_ACCOUNT","ACCOUNT_PASSWORD_ERROR_ONE",request)
         except Exception as e:
               print(e)
               request = self.mainscript.set_message("error","EMPLOYEE_ACCOUNT","ACCOUNT_PASSWORD_ERROR_TWO",request)
         return request

#    Employee Log in
    def employeeSignIn(self,request):
          success = False
          try:
              account = Account.objects.get(user__email=request.POST['email'])
              if check_password(request.POST['password'],account.password):
                   request,success = self.mainscript.login_sesstion(account,request)
              else:
                   request = self.mainscript.set_message("warning","EMPLOYEE_ACCOUNT","ACCOUNT_PASSWORD_ERROR_ONE",request)
          except Exception as e:
                request = self.mainscript.set_message("error","EMPLOYEE_ACCOUNT","ACCOUNT_LOGIN_ERROR",request)
                print(e)
          return request,success