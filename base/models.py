from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Orginization(models.Model):
    orginization_name = models.CharField(max_length=200, unique=True)
    owner_email = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=200)
    semester = models.CharField(max_length=20)
    year = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    orginization = models.ForeignKey(Orginization, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    u_id = models.BigIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[(
        'Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
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


class Lecturer(models.Model):
    orginization = models.ForeignKey(Orginization, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    u_id = models.BigIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[(
        'Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
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
