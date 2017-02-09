from django import forms
import gameshop.settings as settings


class PaymentForm(forms.Form):
    """A payment form designed to work with Simple Payments"""

    pid = forms.CharField(widget=forms.HiddenInput())
    sid = forms.CharField(
        initial=settings.SELLER_ID, widget=forms.HiddenInput())
    amount = forms.CharField(widget=forms.HiddenInput())
    checksum = forms.CharField(widget=forms.HiddenInput())

    # URLs are read from settings
    success_url = forms.CharField(
        initial=settings.PAYMENT_SUCCESS_URL, widget=forms.HiddenInput())
    cancel_url = forms.CharField(
        initial=settings.PAYMENT_CANCEL_URL, widget=forms.HiddenInput())
    error_url = forms.CharField(
        initial=settings.PAYMENT_ERROR_URL, widget=forms.HiddenInput())
