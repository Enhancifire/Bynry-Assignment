from django import forms

from .models import REQUEST_TYPES

class ServiceRequestForm(forms.Form):
    request_type = forms.ChoiceField(choices=REQUEST_TYPES)
    description = forms.CharField(widget=forms.Textarea)
    # attachments = forms.FileField()
