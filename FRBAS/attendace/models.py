from django.db import models
from employee.models import Detail,Status,Employee 
# Create your models here.

ATTENDACE_SHIFT   = [('in',"Work-In"),('ou','Work-Leave')]
LEAVE_PERMISSTION = [('yr', 'Year'),('md', 'Medical'),('br','Child-Birth'),('gr','Grief'),('lv','Leave'),('ot','Other')]
class Attendace(Detail):
     employee  = models.ForeignKey(Employee,on_delete=models.CASCADE,help_text="Employee attendace record ")
     status    = models.CharField("Status",choices=ATTENDACE_SHIFT,max_length=3,help_text="Employee working hour and leave status check")
     late      = models.SmallIntegerField("Late",default=0,help_text="Employee work in time late or not late")
     date      = models.DateField("Date",auto_now_add=True,help_text="Employee attendace recorded date")
     time      = models.TimeField("Time",help_text="Employee Work in or Leave time")
     class Meta:
         unique_together = ('employee','status', 'late')
         
     def __str__(self) -> str:
          return f"{self.employee.fname} attendace on {self.date}"

class Permission(Detail,Status):
     employee    = models.ForeignKey(Employee, on_delete=models.CASCADE,help_text="Employee request permisstion")
     leave       = models.CharField("Leave Type",choices=LEAVE_PERMISSTION,max_length=3,help_text="Employee leave request type")
     detail      = models.CharField("Description",max_length=250,help_text="Employee leave permisstion details")
     start       = models.DateField("Start Date",help_text="Leave start date")
     finish      = models.DateField("End Date",help_text="Leave finish date ")
     autorizer   = models.ForeignKey(Employee,null=True,related_name="autorizer",on_delete=models.CASCADE,help_text="Autorized Employee granted leave permisstion")
     
     class Meta:
         unique_together = ('employee', 'start', 'leave')
         
     def __str__(self) -> str:
          return f"{self.employee.fname} leave on {self.start}"
     
     # Check if new persmisstion request date is b/n older permisstions dates
     def isBetweenDate(self, start, end):
         if self.start <= start <= self.finish:
             return True
         else:
             if self.start > start:
                 if self.start <= end:
                     return True
                 else:
                     return False
             else:
                 return False
     