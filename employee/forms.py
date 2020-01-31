from django import forms
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name',
                  'title',
                  'univercity',
                  'email',
                  'age']

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('age is not valid')
        return age

