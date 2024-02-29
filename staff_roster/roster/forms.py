from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname', 'employee_Id', 'mobile', 'shift')
        labels = {
            'fullname' : 'Full Name',
            'mobile' : 'Mobile Number',
            'employee_Id' : 'Employee Id',
            'shift': 'Shift'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__( *args, **kwargs)
        self.fields['shift'].empty_label = "Select"
        self.fields['employee_Id'].required = False