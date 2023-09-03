# 회원가입 폼 만지기 
from django import forms 
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model=User 
        fields = ["nickname"]
    def signup(self,request,user):
        user.nickname = self.cleaned_data["nickname"]
        user.save() 
# 이후 settings.py에 추가해줘야 한다. 
# ACCOUNT_SIGNUP_FORM_CLASS = "hirestaurant.forms.SignupForm"