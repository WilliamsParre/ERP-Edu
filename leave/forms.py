from django.forms import ModelForm
from .models import Leave

class LeaveForm(ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'