from django.db import models
import datetime
# Create your models here.
GENDER = [
     ('m',"Male"),
     ('f',"Female")
]

CITY =[  
         ("aa", "Addis Ababa"),
         ("naz","Nazrēt"),
         ("god", "Gonder"),
         ("mek","Mekele"),
         ("aws","Āwasa"),
         ("dd","Dire Dawa"),
         ("bah","Bahir Dar"),
         ("har", "Harar"),
         ("jig", "Jijiga"),
         ("aso", "Āsosa"),
         ("gam", "Gambēla"),
         ("sem", "Semera")
    ]

SYSTEM_AUTHORITY = [('ex','Expert'),('ad','Admin'),('ep','Employee')]
class Detail(models.Model):
     pub_date = models.DateTimeField(auto_now_add=True ,null=True,help_text="published date")
     class Meta:
         abstract = True

WORK_START  = datetime.time(2,30,0)
WORK_END    = datetime.time(10,59,0)

class Status(models.Model):
     active = models.PositiveSmallIntegerField(default=1, help_text="active or inactive status")
     trash  = models.PositiveSmallIntegerField(default=0, help_text="deleted or not deleted status")
     class Meta:
         abstract = True
         
class Employee(Detail,Status):
     email     = models.EmailField("Email",unique=True,primary_key=True,help_text="employee unique email account")
     fname     = models.CharField("Full Name ",max_length=100, help_text="employee full name")
     phone     = models.CharField("Phone Number", max_length=10, help_text="employee phone number", unique=True)
     birth     = models.DateField("Date Of Birth", help_text="employee date of birth")
     id        = models.CharField("ID", null=True,max_length=100,  blank=True, help_text="employee compony id")
     gender    = models.CharField("Gender",choices=GENDER, max_length=2, help_text="employee gender")
     coutry    = models.CharField("Country",choices=CITY, max_length=3, help_text="employee currently living country")
     
     def __str__(self) -> str:
          return self.fname

class Account(Detail,Status):
     user     = models.OneToOneField(Employee, on_delete=models.CASCADE,help_text="employee")
     password = models.CharField("Password", max_length=100, help_text="User system access password")
     autority = models.CharField("System Autority",max_length=2, choices=SYSTEM_AUTHORITY, default='ep', help_text="user privilages over system")

     def __str__(self) -> str:
          return self.user.fname

class Department(Detail,Status):
     name    = models.CharField("Name",max_length=50,help_text="department name")
     detail  = models.CharField("Description",max_length=100,blank=True,null=True,help_text="department description")
     depid   = models.CharField("ID",max_length=100,blank=True,null=True,help_text="department id")
     creater = models.ForeignKey(Employee, on_delete=models.CASCADE, help_text="employee with autority create the department") 
     class Meta:
         unique_together = ('name', 'depid')

     def __str__(self) -> str:
          return self.name

class Job(Detail,Status):
     department = models.ForeignKey(Department, on_delete=models.CASCADE,help_text="job created as which part of department")
     title      = models.CharField("Title",max_length=50,help_text="job title")
     detail     = models.CharField("Description",max_length=100,blank=True,null=True,help_text="job description")
     jobid      = models.CharField("ID",max_length=100,blank=True,null=True,help_text="job uniqe identifying id")
     creater    = models.ForeignKey(Employee, on_delete=models.CASCADE, help_text="employee with autority create the job") 
     class Meta:
         unique_together = ('department','title', 'jobid')

     def __str__(self) -> str:
          return self.title

class Work(Detail):
     employee  = models.OneToOneField(Employee, on_delete=models.CASCADE,help_text="employee detail")
     job       = models.ForeignKey(Job,on_delete=models.CASCADE,help_text=" employee job description")
     begin     = models.TimeField("Work Start",default=WORK_START,help_text="employee work start")
     finish    = models.TimeField("Work End",default=WORK_START,help_text="employee work end")
     assigned  = models.ForeignKey(Employee,related_name='assigned', on_delete=models.CASCADE, help_text="employee assigned by which employee autorizesd")

     def __str__(self) -> str:
          return f"{self.employee.fname} works {self.job.title}"