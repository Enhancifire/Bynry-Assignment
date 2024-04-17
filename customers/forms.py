from django import forms

from .models import Customer


class CustomerProfileForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField()
