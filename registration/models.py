from django.db import models
from base.models import Course, Organization, Faculty
# Create your models here.

# class FacultyCourseRegistration(models.Model):
#     course = models.ManyToManyField(Course)


class Section(models.Model):
    s_id = models.BigAutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    strength = models.PositiveIntegerField()

    def __str__(self):
        return str(self.s_id)
