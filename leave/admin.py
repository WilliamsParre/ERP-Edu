from django.contrib import admin
from django.utils.html import format_html
from .models import Leave, NonTeachingLeave
# from .models import LeaveBalance, NonTeachingLeaveBalance
# Register your models here.

# class FacultyLeaveBalanceAdmin(admin.ModelAdmin):
#     list_display = ('e_id', 'leave_type', 'available_days', 'allocated_days')
#     list_filter = ('leave_type',)
class FacultyLeaveAdmin(admin.ModelAdmin):
    list_display = ('e_id', 'first_name','last_name','leave_type', 'requested_days', 'leave_Status')
    list_filter = ('leave_Status', 'leave_type', 'requested_days')    

class NonTeachingLeaveAdmin(admin.ModelAdmin):
    list_display = ('e_id', 'first_name','last_name','leave_type', 'requested_days', 'leave_Status')
    list_filter = ('leave_Status', 'leave_type', 'requested_days')

admin.site.register(Leave, FacultyLeaveAdmin)
# admin.site.register(LeaveBalance, FacultyLeaveBalanceAdmin)
admin.site.register(NonTeachingLeave, NonTeachingLeaveAdmin)
# admin.site.register(NonTeachingLeaveBalance, NonTeachingLeaveBalanceAdmin)