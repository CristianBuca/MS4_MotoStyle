# Imports
# 3rd party:
from django import forms
# Internal
from .models import Product, Category
from .widgets import CustomClearableFileInput
# -----------------------------------------------------------------------------


class ProductForm(forms.ModelForm):
    """
    Class defining the form for Product management
    """
    class Meta:
        model = Product
        fields = (
            'category', 'sku', 'name', 'description', 'price',
            'rating', 'image_url', 'image', 'has_sizes'
        )

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize method for the form
            Arguments:
                self (object): The object initialized
                *args: other arguments
                **kwargs: keyword arguments
            Returns:
                N/A
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
