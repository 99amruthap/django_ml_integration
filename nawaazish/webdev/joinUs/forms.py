from django import forms
from .models import JoinUs

class JoinUsForm(forms.ModelForm):
    class Meta:
        model = JoinUs
        fields = '__all__'

