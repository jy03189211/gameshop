from django import forms
import gameshop.settings as settings


class PaymentForm(forms.Form):
    """A payment form designed to work with Simple Payments"""

    pid = forms.CharField(widget=forms.HiddenInput())
    sid = forms.CharField(widget=forms.HiddenInput())
    amount = forms.CharField(widget=forms.HiddenInput())
    checksum = forms.CharField(widget=forms.HiddenInput())
    # payment service will be bypassed for zero amount payments,
    # thus allow urls to be omitted
    success_url = forms.CharField(widget=forms.HiddenInput(), required=False)
    cancel_url = forms.CharField(widget=forms.HiddenInput(), required=False)
    error_url = forms.CharField(widget=forms.HiddenInput(), required=False)
