from django.contrib import messages
from configparser import ConfigParser
import os
from pathlib import Path

class FrbasScript:
    def __init__(self) -> None:
      self.config = ConfigParser()
      self.config.read(f'{os.path.join(Path(__file__).resolve().parent,"configration")}/frbas_text_config.cfg')
         
#   set message to request value
    def set_message(self, type,catagory, msg, request):
        if type == 'success':
             messages.add_message(request, messages.SUCCESS, self.config.get(catagory, msg))
        elif type == 'info':
             messages.add_message(request, messages.INFO, self.config.get(catagory, msg))
        elif type == 'warning':
             messages.add_message(request, messages.WARNING, self.config.get(catagory, msg))
        else:
             messages.add_message(request, messages.ERROR, self.config.get(catagory, msg))
        
        return request

#    Employee Log in sesstion create
    def login_sesstion(self,account,request):
         success = False
         try:
              request.session['user_email'] = account.user.email
              request.session['user_autority'] = account.autority
              request = self.set_message("success","EMPLOYEE_ACCOUNT","ACCOUNT_LOGIN_SUCCESS",request)
              success = True
         except Exception as e:
              print(e)
              request = self.set_message("error","DEFAULT","SESSTION_ERROR",request)
         return request ,success
    
#    Get Sesstion Value
    def sesstionValueGet(self,value,request):
        if value == 'email':
             return request.session.get('user_email',False)
        if value == 'authority':
             return request.session.get('user_autority',False)
    
#    Create your views here.
    def log_out(self,request):
        for key in list(request.session.keys()):
             del request.session[key]
        return request
   