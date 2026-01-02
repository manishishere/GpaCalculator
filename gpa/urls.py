from django.contrib import admin
from django.urls import path
from gpa.views import login_view,register,gpaCalculate,finalgpa,update,delete,home

urlpatterns = [
    path('login/',login_view,name='login'),
    path('register/',register,name='register'),
    path('calculate/',gpaCalculate,name='gpaCalculate'),
    path('finalgpa/',finalgpa,name='finalGpa'),
    path('home/',home,name='home'),
    path('update/<int:id>/',update,name='updateGpa'),
    path('delete/<int:id>/',delete,name='delete'),
    
]