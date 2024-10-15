from django.forms import ModelForm
from .models import Lead

class LeadCreation(ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'