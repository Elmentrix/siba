from django import forms
from django.forms import ModelForm
from .models import student_db

# class for form instance
class student_form(ModelForm):
    class Meta:
        model = student_db
        # fields = '__all__'
        fields = ('student_Id', 'name', 'age', 'gender')
        widgets = {
            'student_Id': forms.TextInput(attrs = {'class': 'form-control'}),
            'name': forms.TextInput(attrs = {'class': 'form-control'}),
            'age': forms.TextInput(attrs = {'class': 'form-control'}),
            'gender': forms.Select(attrs = {'class': 'form-control'}),
        }