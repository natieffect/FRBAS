from django.urls import path
from .import views

app_name = 'employee'
urlpatterns = [
    path("",views.employeeSignIn,name="signIn"),
    path("signup/",views.employeeSignUp,name="signup"),
]