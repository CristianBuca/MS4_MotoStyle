# Imports
# 3rd party:
from django import forms
# Internal
from .models import Order
# -----------------------------------------------------------------------------


class OrderForm(forms.ModelForm):
    """
    Class defining the fields and methods used on the Order Form
    """
    class Meta:
        """
        Defines the Meta fields on the Order Form
        """
        model = Order
        field = (
            'full_name', 'email', 'phone_number', 'address_line1',
            'address_line2', 'town_or_city', 'area', 'postcode', 'country',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
            Arguments: self (object): The object using the method
            Returns: N/A
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'area': 'Area',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
