# Imports
# 3rd party:
from django.test import TestCase
# Internal
from .models import BlogPost, Comment
# -----------------------------------------------------------------------------

class TestBlogModels(TestCase):
    """
    Defines the models unit tests for the blog app
    """

    def test_blogpost_str(self):
        """
        Tests if BlogPost model str method returns correct string
        """