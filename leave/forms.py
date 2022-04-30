from django.forms import ModelForm
from .models import Leave, NonTeachingLeave

class LeaveForm(ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'

class NonTeachingLeaveForm(ModelForm):
    class Meta:
        model = NonTeachingLeave
        fields = '__all__'