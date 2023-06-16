from .models import Employee,GENDER,CITY
from django.contrib.auth.hashers import make_password, check_password
from frbasScript import  FrbasScript


class EmployeeScript:
    def __init__(self) -> None:
         self.mainscript = FrbasScript()
    
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
             
             request = self.mainscript.set_message("success","EMPLOYEE_SIGN_UP","SIGNUP_SUCCESS",request)
        except Exception as e: 
             print(e)
             request = self.mainscript.set_message("error","EMPLOYEE_SIGN_UP","SIGNUP_ERROR",request)
        return request
   
#     Employee Gender Display
    def employeeGender(self):
         gender = []
         for value in GENDER:
              gender.append({'value': value[0], 'name':value[1]})
         return gender
    
#     Employee Country Display 
    def employeeCountry(self):
         country = []
         for value in CITY:
              country.append({'value': value[0], 'name':value[1]})
         return country
         
         