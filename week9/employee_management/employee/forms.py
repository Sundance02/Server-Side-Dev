from django import forms
from .models import *

class EmployeeForm(forms.Form):
    first_name  = forms.CharField(label="First_Name", max_length=100)
    last_name  = forms.CharField(label="Last_Name", max_length=100)
    gen_choices =  (
        ('M', 'M'),
        ('F', 'F'),
        ('LGBT', 'LGBT'),
    )
    gender = forms.ChoiceField(choices=gen_choices)
    birth_date = forms.DateField(label="Birth_Date", widget=forms.TextInput(attrs={"type":"date"}))
    hire_date  = forms.DateField(label="Hire_Date", widget=forms.TextInput(attrs={"type":"date"}))
    salary  = forms.DecimalField(label="Salary")
    position = forms.ModelChoiceField(
        queryset = Position.objects.all()
    )
