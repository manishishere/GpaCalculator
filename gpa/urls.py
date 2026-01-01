from django.contrib import admin
from django.urls import path
from gpa.views import login_view,register,gpaCalculate,finalgpa,update,delete

urlpatterns = [
    path('login/',login_view,name='login'),
    path('register/',register,name='register'),
    path('calculate/',gpaCalculate,name='gpaCalculate'),
    path('finalgpa/',finalgpa,name='finalGpa'),
    path('update/<int:id>/',update,name='updateGpa'),
    path('delete/<int:id>/',delete,name='delete'),
    
]