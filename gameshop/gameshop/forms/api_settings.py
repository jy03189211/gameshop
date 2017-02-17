import re
from django import forms
from gameshop.models import User


class ApiSettingsForm(forms.Form):
    """Used in changing the users' allowed hosts for API requests"""

    api_hosts = forms.CharField(
        max_length=512,
        required=False,
        label="Allowed domains",
        help_text='API requests from these domains are allowed. Use "*" to \
        allow all, or specify a comma-separated list of domains.')

    def clean_api_hosts(self):
        """
        Validate that the host list is properly formatted.

        NOTE: this only validates comma-separability and characters,
              and does not actually separate the data for the model.
              User the User.get_api_host_list method for that.
        """

        value = self.cleaned_data['api_hosts']

        try:
            # check allowed characters
            # NOTE: there's a space at the end of the regex
            if not re.match("^[\w.,:;$\-_+!*\'()/?@=& ]*$", value):
                raise forms.ValidationError('Disallowed characters', code='invalid')

            # separate at commas
            value = [i.strip() for i in value.split(',') if i.strip()]

            if len(value) < 1:
                raise forms.ValidationError('Must not be empty', code='invalid')

            print('hosts valid')

            # return the same if no errors
            return self.cleaned_data['api_hosts']

        except:
            print('hosts not valid')

            raise forms.ValidationError('Check the format of the list. \
                The special characters allowed are: .,:;$-_+!*\'()/?@=&', code='invalid')
