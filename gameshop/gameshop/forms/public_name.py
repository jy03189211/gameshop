from django import forms


class PublicNameForm(forms.Form):
    """Used in changing the public name of the user"""

    public_name = forms.CharField(max_length=50, required=False,
        help_text='The public name will be shown as the developer\'s name for the games you add.')
