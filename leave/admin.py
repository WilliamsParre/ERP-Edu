from django.contrib import admin
from .models import Leave, NonTeachingLeave
# from .models import LeaveBalance, NonTeachingLeaveBalance
# Register your models here.

class FacultyLeaveBalanceAdmin(admin.ModelAdmin):
    list_display = ('e_id', 'leave_type', 'available_days', 'allocated_days')
class FacultyLeaveAdmin(admin.ModelAdmin):
    list_display = ('e_id', 'first_name','last_name','leave_type', 'requested_days', 'leave_Status')
    

class NonTeachingLeaveBalanceAdmin(admin.ModelAdmin):
    list_display = ('e_id', 'leave_type', 'available_days', 'allocated_days')
class NonTeachingLeaveAdmin(admin.ModelAdmin):
    list_display = ('e_id', 'first_name','last_name','leave_type', 'requested_days', 'leave_Status')

admin.site.register(Leave, FacultyLeaveAdmin)
# admin.site.register(LeaveBalance, FacultyLeaveBalanceAdmin)
admin.site.register(NonTeachingLeave, NonTeachingLeaveAdmin)
# admin.site.register(NonTeachingLeaveBalance, NonTeachingLeaveBalanceAdmin)