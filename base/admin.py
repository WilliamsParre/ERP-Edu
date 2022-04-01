from django.contrib import admin

# Register your models here.

from .models import Course, Student

admin.site.site_header = 'ERP - Admin'
admin.site.site_title = 'ERP'
admin.site.index_title = 'Welcome to ERP Administration'


class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description',
                    'semester', 'year', 'created')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('u_id', 'first_name', 'last_name',
                    'gender', 'email', 'mobile')


admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
