# Imports
# 3rd party:
from django.test import TestCase
# Internal
from .forms import BlogPostForm, CommentForm
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

    def test_blog_post_form_no_content(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with empty content field
        Tests if form fails validation
        """
        form = BlogPostForm({
            'title': 'Test Blog Post',
            'content': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(
            form.errors['content'][0], 'This field is required.'
        )

    def test_blog_post_form_is_valid(self):
        """
        Test if form validates correctly when required fields are filled in
        """
        form = BlogPostForm({
            'title': 'Test Blog Post',
            'content': 'Test Blog Post Content'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_no_comment_body(self):
        """
        Tests if correct error is displayed to the user when
        trying to submit form with empty comment_body field
        Tests if form fails validation
        """
        form = CommentForm({
            'comment_body': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('comment_body', form.errors.keys())
        self.assertEqual(
            form.errors['comment_body'][0], 'This field is required.'
        )

