from django import forms
from .models import Event

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['full_name', 'email', 'phone']

    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100, required=True)
    phone = forms.CharField(max_length=20)
