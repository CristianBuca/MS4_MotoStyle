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
        fields = (
            'owner', 'title', 'content', 'image_url', 'image',
            'second_image_url', 'second_image', 'third_image_url',
            'third_image', 'fourth_image_url', 'fourth_image',
            'fifth_image_url', 'fifth_image',
        )

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
