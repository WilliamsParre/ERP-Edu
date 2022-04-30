from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Orginization, Student, Lecturer, NonTeaching


class signUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


class OrginizationRegistrationForm(ModelForm):
    class Meta:
        model = Orginization
        fields = '__all__'


class StudentRegistriationForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class FacultyRegistriationForm(ModelForm):
    class Meta:
        model = Lecturer
        fields = '__all__'

class NonTeachingFacultyRegistriationForm(ModelForm):
    class Meta:
        model = NonTeaching
        fields = '__all__'
