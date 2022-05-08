from turtle import update
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Course, Organization, Student, Faculty, NonTeaching


class signUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


class OrganizationRegistrationForm(ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'


class StudentRegistriationForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class FacultyRegistriationForm(ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'


class NonTeachingFacultyRegistriationForm(ModelForm):
    class Meta:
        model = NonTeaching
        fields = '__all__'


class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'email')


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ('organization',)
