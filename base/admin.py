from django.contrib import admin

# Register your models here.

from .models import Course, Student, Lecturer,NonTeaching, Branch, Orginization

admin.site.site_header = 'ERP - Admin'
admin.site.site_title = 'ERP'
admin.site.index_title = 'Welcome to ERP Administration'


class OrginisationAdmin(admin.ModelAdmin):
    list_display = ('orginization_name', 'owner')


class BranchAdmin(admin.ModelAdmin):
    list_display = ('orginization', 'name')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description','orginization',
                    'semester', 'year', 'created')


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('e_id', 'first_name', 'last_name',
                    'gender', 'orginization', 'email', 'mobile')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('u_id', 'first_name', 'last_name',
                    'gender', 'orginization', 'email', 'mobile')
    
class NonTeachingAdmin(admin.ModelAdmin):
    list_display = ('nt_e_id', 'first_name', 'last_name',
                    'gender', 'orginization', 'email', 'mobile')
    


admin.site.register(Orginization, OrginisationAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(NonTeaching, NonTeachingAdmin)