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
    def test_blog(self):
        """
        Tests if blog page is accessible with status code of 200
        Tests if blog view renders blog.html
        """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')
