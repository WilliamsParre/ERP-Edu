from django.contrib import admin

# Register your models here.

from .models import Course, Student, Lecturer, Orginization

admin.site.site_header = 'ERP - Admin'
admin.site.site_title = 'ERP'
admin.site.index_title = 'Welcome to ERP Administration'


class OrginisationAdmin(admin.ModelAdmin):
    list_display = ('orginization_name', 'owner')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description',
                    'semester', 'year', 'created')


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('e_id', 'first_name', 'last_name',
                    'gender', 'email', 'mobile')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('u_id', 'first_name', 'last_name',
                    'gender', 'email', 'mobile')


admin.site.register(Orginization, OrginisationAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Student, StudentAdmin)
