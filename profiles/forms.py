# Imports
# 3rd party:
from django import forms
# Internal
from .models import UserProfile
# -----------------------------------------------------------------------------


class UserProfileForm(forms.ModelForm):
    """
    Class defining the fields and methods used on the user profile form
    """
    class Meta:
        """
        Defines the Meta fields on the user profile form
        """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes and set autofocus on phone field
            Arguments: self (object): The object using the method
            Returns: N/A
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_address_line1': 'Address Line 1',
            'default_address_line2': 'Address Line 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postal Code',
            'default_area': 'Area',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'profile-form-input'
                self.fields[field].label = True
                self.fields[field].label = placeholder.__str__()
