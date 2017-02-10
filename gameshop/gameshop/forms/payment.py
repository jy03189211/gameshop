from django import forms
import gameshop.settings as settings


class PaymentForm(forms.Form):
    """A payment form designed to work with Simple Payments"""

    pid = forms.CharField(widget=forms.HiddenInput())
    sid = forms.CharField(widget=forms.HiddenInput())
    amount = forms.CharField(widget=forms.HiddenInput())
    checksum = forms.CharField(widget=forms.HiddenInput())
    success_url = forms.CharField(widget=forms.HiddenInput())
    cancel_url = forms.CharField(widget=forms.HiddenInput())
    error_url = forms.CharField(widget=forms.HiddenInput())
