from django.contrib import admin

# Register your models here.

from .models import Course, Student, Faculty, NonTeaching, Branch, Organization

admin.site.site_header = 'ERP - Admin'
admin.site.site_title = 'ERP'
admin.site.index_title = 'Welcome to ERP Administration'


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'owner')


class BranchAdmin(admin.ModelAdmin):
    list_display = ('organization', 'name')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description', 'organization',
                    'semester', 'year', 'created')
    list_filter = ('year', 'semester')


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('e_id', 'first_name', 'last_name',
                    'gender', 'organization', 'email', 'mobile')
    list_filter = ('gender',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('u_id', 'first_name', 'last_name',
                    'gender', 'organization', 'email', 'mobile')
    list_filter = ('gender',)


class NonTeachingAdmin(admin.ModelAdmin):
    list_display = ('nt_e_id', 'first_name', 'last_name',
                    'gender', 'organization', 'email', 'mobile')
    list_filter = ('gender',)


admin.site.register(Organization, OrganisationAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Faculty, LecturerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(NonTeaching, NonTeachingAdmin)
