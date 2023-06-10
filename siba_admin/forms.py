from django import forms
from django.forms import ModelForm
from .models import Courses, Assignments, Subjects
from siba_student.models import student_db

# forms for courses
class Courses_forms(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('course_Id', 'course_name')
        widgets = {
            'course_Id': forms.TextInput(attrs = {'class': 'form-control'}),
            'course_name': forms.TextInput(attrs = {'class': 'form-control'}),
        }


# forms for assigning
class Assignments_form(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Courses.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    student = forms.ModelChoiceField(queryset=(student_db.objects.all()), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Assignments
        fields = ('student', 'course')


# subject forms
class subject_form(forms.ModelForm):
    course_alloc = forms.ModelChoiceField(queryset=Courses.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Subjects
        fields = ('subject', 'course_alloc')
        widgets = {
            'subject': forms.TextInput(attrs = {'class': 'form-control'})
        }