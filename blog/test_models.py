# Imports
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
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
        user = User.objects.create_user(
            username='unit_test_user', password='unit_test_pass'
        )
        self.client.login(
            username='unit_test_user', password='unit_test_pass'
        )
        blog_post = BlogPost.objects.create(
            title='Test Blog Post',
            content='Test Blog Post content',
            owner=user,
        )
        self.assertEqual(blog_post.__str__(), blog_post.title)
