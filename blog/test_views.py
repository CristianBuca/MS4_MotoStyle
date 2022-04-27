# Imports
# 3rd party:
from django.test import TestCase
# Internal
from .models import BlogPost, Comment
# -----------------------------------------------------------------------------


class TestBlogViews(TestCase):
    """
    Defines the views unit tests for the blog app
    """
    