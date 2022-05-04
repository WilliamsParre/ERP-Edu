from django.forms import ModelForm
from .models import Leave, NonTeachingLeave

class LeaveForm(ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'
        exclude = ('leave_Status',)

class NonTeachingLeaveForm(ModelForm):
    class Meta:
        model = NonTeachingLeave
        fields = '__all__'
        exclude = ('leave_Status',)