from django.db import models
from base.models import Faculty, NonTeaching
# Create your models here.


class Leave(models.Model):
    class LeaveRequestChoices(models.TextChoices):
        Personal_Leave = 'Personal'
        Annual_Leave = 'Annual'
        Military_Leave = 'Military'
        Pregnancy_Disability_Leave = 'PDL'

    class LeaveStatusChoices(models.TextChoices):
        Pending_Status = 'Pending'
        Approved_Status = 'Approved'
        Declined_Status = 'Declined'
        Cancelled_Status = 'Cancelled'

    id = models.BigAutoField(primary_key=True)
    e_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    leave_type = models.CharField(
        max_length=10, choices=LeaveRequestChoices.choices)
    start_date = models.DateField(help_text='Leave begin date')
    end_date = models.DateField(help_text='Leave end date')
    requested_days = models.PositiveIntegerField(
        default=0, help_text='Total no of leave days requested')
    leave_Status = models.CharField(
        max_length=10, choices=LeaveStatusChoices.choices, default=LeaveStatusChoices.Pending_Status)
    reason = models.CharField(max_length=500, null=True)

    def __str__(self):
        return '%s %s %s' % (self.e_id, self.first_name, self.last_name)


class NonTeachingLeave(models.Model):
    class LeaveRequestChoices(models.TextChoices):
        Personal_Leave = 'Personal'
        Annual_Leave = 'Annual'
        Military_Leave = 'Military'
        Pregnancy_Disability_Leave = 'PDL'

    class LeaveStatusChoices(models.TextChoices):
        Pending_Status = 'Pending'
        Approved_Status = 'Approved'
        Declined_Status = 'Declined'
        Cancelled_Status = 'Cancelled'

    id = models.BigAutoField(primary_key=True)
    e_id = models.ForeignKey(NonTeaching, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    leave_type = models.CharField(
        max_length=10, choices=LeaveRequestChoices.choices)
    start_date = models.DateField(help_text='Leave begin date')
    end_date = models.DateField(help_text='Leave end date')
    requested_days = models.PositiveIntegerField(
        default=0, help_text='Total no of leave days requested')
    leave_Status = models.CharField(
        max_length=10, choices=LeaveStatusChoices.choices, default=LeaveStatusChoices.Pending_Status)
    reason = models.CharField(max_length=500, null=True)

    def __str__(self):
        return '%s %s %s' % (self.e_id, self.first_name, self.last_name)

# class LeaveBalance(models.Model):
#     class LeaveRequestChoices(models.TextChoices):
#         Personal_Leave = 'Personal'
#         Annual_Leave = 'Annual'
#         Military_Leave = 'Military'
#         Pregnancy_Disability_Leave = 'PDL'

#     e_id = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
#     leave_type = models.CharField(max_length=10, choices=LeaveRequestChoices.choices)
#     available_days = models.PositiveIntegerField(default=0, help_text='Remaining/available leave days per employee')
#     allocated_days = models.PositiveIntegerField(default=0, help_text='No of leave days allocated to a leave type per '
#                                                                       'employee per year')

#     def __str__(self):
#         return '%s %s' % (self.e_id, self.leave_type)

# class NonTeachingLeaveBalance(models.Model):
#     class LeaveRequestChoices(models.TextChoices):
#         Personal_Leave = 'Personal'
#         Annual_Leave = 'Annual'
#         Military_Leave = 'Military'
#         Pregnancy_Disability_Leave = 'PDL'

#     e_id = models.ForeignKey(NonTeaching, on_delete=models.CASCADE)
#     leave_type = models.CharField(max_length=10, choices=LeaveRequestChoices.choices)
#     available_days = models.PositiveIntegerField(default=0, help_text='Remaining/available leave days per employee')
#     allocated_days = models.PositiveIntegerField(default=0, help_text='No of leave days allocated to a leave type per '
#                                                                       'employee per year')

#     def __str__(self):
#         return '%s %s' % (self.e_id, self.leave_type)
