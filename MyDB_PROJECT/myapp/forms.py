from .models import Student,Proxy_Student
from django import forms
#create Student form
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
class Proxy_StudentForm(forms.ModelForm):
    class Meta:
        model=Proxy_Student
        fields='__all__'
