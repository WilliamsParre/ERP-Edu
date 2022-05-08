from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
# Create your models here.


class Orginization(models.Model):
    orginization_name = models.CharField(max_length=200, unique=True)
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.orginization_name


class Branch(models.Model):
    orginization = models.OneToOneField(Orginization, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name+' ---> '+str(self.orginization)


class Course(models.Model):
    orginization = models.ForeignKey(Orginization, on_delete=models.CASCADE)
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=200)
    semester = models.CharField(max_length=20)
    year = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        x = str(self.branch).split('--->')
        x = x[1].strip()
        print(x)
        print(x == str(self.orginization))
        if x == str(self.orginization):
            super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Student(models.Model):
    orginization = models.ForeignKey(Orginization, on_delete=models.CASCADE)
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.first_name+' '+self.last_name


class Lecturer(models.Model):
    orginization = models.ForeignKey(Orginization, on_delete=models.CASCADE)
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    e_id = models.BigIntegerField()
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

    def __str__(self):
        return self.first_name+' '+self.last_name


class NonTeaching(models.Model):
    orginization = models.ForeignKey(Orginization, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nt_e_id = models.BigIntegerField()
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

    def __str__(self):
        return self.first_name+' '+self.last_name
