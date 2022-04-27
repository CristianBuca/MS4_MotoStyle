# Imports
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
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

    def test_get_blog_post(self):
        """
        Tests if blog_post page is accessible with status code of 200
        Tests if blog_post view renders blog_post.html
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
        response = self.client.get(f'/blog/{blog_post.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_post.html')
