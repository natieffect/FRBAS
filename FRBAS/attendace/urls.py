from django.urls import path
from .import views

app_name = 'attendace'
urlpatterns = [
     path('leave/',views.attendacePermisstionAdd,name="leave"),
     ]