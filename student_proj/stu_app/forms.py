from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'sid':'STUDENT ID',
            'sname':'STUDENT NAME',
            'city':'CITY',
            'marks':'MARKS'
        }