from django import forms
from testApp import models

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=models.Employee
        fields="__all__"
