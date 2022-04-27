# Imports
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
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

    def test_user_post_add_blog_post(self):
        """
        Tests if user can add blog post
        Tests if user is redirected to the blog page
        Tests if toast displays correct message
        """
        user = User.objects.create_user(
            username='unit_test_user', password='unit_test_pass'
        )
        self.client.login(
            username='unit_test_user', password='unit_test_pass'
        )
        response = self.client.post('/blog/add/', {
            'title': 'Test Add Blog Post',
            'content': 'Test Add Blog Post content',
            'owner': user,
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(
            messages[0]), 'Your article has been posted.'
        )
        self.assertRedirects(response, '/blog/')

    def test_user_post_edit_blog_post(self):
        """
        Tests if user can edit their own blog post
        Tests if user is redirected to the blog post page
        Tests if toast displays correct message
        """
        user = User.objects.create_user(
            username='unit_test_user', password='unit_test_pass'
        )
        blog_post = BlogPost.objects.create(
            title='Test Blog Post',
            content='Test Blog Post content',
            owner=user,
        )
        self.client.login(
            username='unit_test_user', password='unit_test_pass'
        )
        response = self.client.post(f'/blog/edit/{blog_post.id}/', {
            'title': 'Test Edit Blog Post',
            'content': 'Test Edit Blog Post content',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(
            messages[0]), 'Changes have been saved'
        )
        self.assertRedirects(response, '/blog/1/')

    