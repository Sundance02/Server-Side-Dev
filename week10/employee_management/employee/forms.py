from django.forms import ModelForm, DateField, Textarea
from django.forms.widgets import TextInput, Textarea
from django.core.exceptions import ValidationError
from employee.models import *
from datetime import date

class EmployeeForm(ModelForm):
    birth_date = DateField(widget= TextInput(attrs={"type":"date"}))
    hire_date = DateField(widget= TextInput(attrs={"type":"date"}))

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'gender', 'birth_date', 'hire_date', 'salary', 'position']

    def clean_hire_date(self):
        data = self.cleaned_data["hire_date"]
        if data > date.today():
            raise ValidationError("hiredate must not be future time")

        return data
    

class ProjectForm(ModelForm):
    start_date = DateField(widget= TextInput(attrs={"type":"date"}))
    due_date = DateField(widget= TextInput(attrs={"type":"date"}))

    class Meta:
        model = Project
        fields = ['name', 'manager', 'due_date', 'start_date', 'description']

    def clean(self):
        # ข้อมูลที่ user กรอกมา
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        due_date = cleaned_data.get("due_date")

        if due_date < start_date:
            raise ValidationError("Start date must not over Due date")
        
        return cleaned_data
    
class ProjectDetailForm(ModelForm):
        start_date = DateField(widget= TextInput(attrs={"type":"date"}))
        due_date = DateField(widget= TextInput(attrs={"type":"date"}))
        description = Textarea()
        class Meta:
            model = Project
            fields = ['name', 'due_date', 'start_date', 'description' ,'manager', 'staff']

        def clean(self):
            # ข้อมูลที่ user กรอกมา
            cleaned_data = super().clean()
            start_date = cleaned_data.get("start_date")
            due_date = cleaned_data.get("due_date")

            if due_date < start_date:
                raise ValidationError("Start date must not over Due date")
            
            return cleaned_data