from .models import Details
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MenuCreateForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['s_name','s_grade','s_credit']
        widgets = {
            's_name':forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Enter subject name..'}),
            's_grade':forms.Select(attrs={'class':'form-control mb-2'}),
            's_credit':forms.NumberInput(attrs={'class':'form-control mb-2', 'placeholder':'Enter credit hour?..'}),
        }

        labels = {
            's_name':'Subject Name',
            's_grade':'Obtained Grade',
            's_credit':'Subject Credit'

        }

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control mb-2'}))
    last_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']
