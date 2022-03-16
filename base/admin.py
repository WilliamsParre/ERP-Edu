from django.contrib import admin

# Register your models here.

from .models import Course, Student

admin.site.site_header = 'ERP Admin Panel'

class StudentAdmin(admin.ModelAdmin):
    list_display = ('u_id','first_name','last_name','gender','email', 'mobile')


admin.site.register(Course)
admin.site.register(Student, StudentAdmin)
