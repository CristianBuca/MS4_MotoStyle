# Imports
# 3rd party:
from django.test import TestCase
# Internal
from .forms import BlogPostForm
# -----------------------------------------------------------------------------


class TestBlogPostForm(TestCase):
    """
    Defines the forms unit tests for the blog app
    """

    def test_blog_post_form_no_title(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with empty title field
        Tests if form fails validation
        """
        form = BlogPostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(
            form.errors['title'][0], 'This field is required.'
        )
