import re
from django import forms


class ApiSettingsForm(forms.Form):
    """Used in changing the users' allowed hosts for API requests"""

    api_key = forms.CharField(
        max_length=512,
        required=False,
        disabled=True,
        label="API key",
        help_text='Your API key is required with every external API request. \
        All requests must be POST requests with "api_key" in the request data.')

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
            if not re.match("^[\w.,:;$\-_+!*\'()/?@=&]*$", value):
                raise forms.ValidationError('Disallowed characters')
            # separate
            value = [i.strip() for i in value.split(',') if i.strip()]
            # return the same if no errors
            return self.cleaned_data['api_hosts']

        except Exception as e:
            raise forms.ValidationError('Check the format of the list. \
            The special characters allowed are: .,:;$-_+!*\'()/?@=&')
