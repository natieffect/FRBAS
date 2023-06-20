from django.shortcuts import render
from decorators import is_loged_out
from .script import AttendaceHandler
# Create your views here.

#   Employee request permisstion 
@is_loged_out
def attendacePermisstionAdd(request):
    attendaceHandler = AttendaceHandler()
    if request.method == "POST":
           request = attendaceHandler.attendacePermisstionAdd(request)
    context = {"attendaceLeave":attendaceHandler.atttendacLeaveValues()}
    return render(request,"attendace/attendacePermisstionAdd.html",context)

