# Imports
# 3rd party:
from django import forms
# Internal
from .models import BlogPost, Comment
from .widgets import CustomClearableFileInput
# -----------------------------------------------------------------------------


class BlogPostForm(forms.ModelForm):
    """
    Class defining the form for BlogPost management
    """
    class Meta:
        model = BlogPost
        fields = (
            'title', 'content', 'image_url', 'image',
            'second_image_url', 'second_image', 'third_image_url',
            'third_image', 'fourth_image_url', 'fourth_image',
            'fifth_image_url', 'fifth_image',
        )
        exclude = ['owner', 'created_at']

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )
    second_image = forms.ImageField(
        label='Second image', required=False, widget=CustomClearableFileInput
    )
    third_image = forms.ImageField(
        label='Third image', required=False, widget=CustomClearableFileInput
    )
    fourth_image = forms.ImageField(
        label='Fourth image', required=False, widget=CustomClearableFileInput
    )
    fifth_image = forms.ImageField(
        label='Fifth image', required=False, widget=CustomClearableFileInput
    )


class CommentForm(forms.ModelForm):
    """
    Class defining the form for blog post comments
    """
    class Meta:
        model = Comment
        fields = (
            'comment_body',
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
        self.fields['comment_body'].label = 'Post your comment:'
