from distutils.command.upload import upload
from pyexpat import model
from turtle import mode, update
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=200)
    semester = models.CharField(max_length=20)
    year = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    u_id = models.BigIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[('Male','Male'), ('Female', 'Female'), ('Others', 'Others')])
    profile_pic = models.ImageField(upload_to='base/templates/', blank=True)
    mobile = models.BigIntegerField()
    blood = models.CharField(max_length=5)
    parent_name = models.CharField(max_length=200)
    parent_mobile = models.BigIntegerField()
    relation = models.CharField(max_length=200)
    cast = models.CharField(max_length=20)
    birth_place = models.CharField(max_length=20)
    height = models.IntegerField()
    weight = models.IntegerField()
    nationality = models.CharField(max_length=40)
    admission_date = models.DateField()





    

