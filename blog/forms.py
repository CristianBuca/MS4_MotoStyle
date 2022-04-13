# Imports
# 3rd party:
from django import forms
# Internal
from .models import BlogPost
from products.widgets import CustomClearableFileInput
# -----------------------------------------------------------------------------


class BlogPostForm(forms.ModelForm):
    """
    Class defining the form for BlogPost management
    """
    class Meta:
        model = BlogPost

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )
    second_image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )
    third_image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )
    fourth_image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )
    fifth_image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )
