from .models import *
from frbasScript import FrbasScript
from script.frbasScriptTime import FrbasScriptTimeDate
class AttendaceHandler:
    def __init__(self) -> None:
         self.frbasScript = FrbasScript()
         self.timeDateValue  = FrbasScriptTimeDate()

#   Employee attendace permisstion Leave values convert to dictionaries
    def atttendacLeaveValues(self):
        leaveValues = []
        for val in LEAVE_PERMISSTION:
            leaveValues.append({"value":val[0],"show":val[1]})
        return leaveValues

#   Employee request leave permisstion handler
    def attendacePermisstionAdd(self,request):
        try:
            permisstion = Permission(employee = Employee.objects.get(email = request.POST.get('email')),
                                     leave    = request.POST.get('leave'),
                                     detail   = request.POST.get('detail'),
                                     start    = request.POST.get('start'),
                                     finish   = request.POST.get('finish'))
            permisstion.save()
            request = self.frbasScript.set_message("success","ATTENDACE_PERMISSTION","PERMISSTION_ADD_SUCCESS",request)
        except Exception as e:
            print(e)
            request = self.frbasScript.set_message("error","ATTENDACE_PERMISSTION","PERMISSTION_ADD_ERROR",request)
        return request