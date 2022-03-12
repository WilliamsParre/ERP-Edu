from turtle import mode, update
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    desception = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=200)
    semester = models.CharField(max_length=20)
    year = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
