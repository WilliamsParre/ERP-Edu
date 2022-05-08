from cProfile import label
from django.contrib import admin
from .models import Section
# Register your models here.


class SectionAdmin(admin.ModelAdmin):
    list_display = ('s_id', 'organization', 'course', 'faculty', 'strength')
    list_filter = ('organization', 'course', 'faculty', 'strength')


admin.site.register(Section, SectionAdmin)
