# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404
# Internal:
from .models import BlogPost
# -----------------------------------------------------------------------------


def blog(request):
    """
    View to render the blog page
        Arguments: request (object): The Http request
        Returns: render blog page with context
    """

    blog = BlogPost.objects.all()
    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)


def blog_post(request, blog_post_id):
    """
    View to render blog posts
        Arguments:
            request (object): The Http request
            blog_post_id: ID of the blog post being viewed
        Returns: render blog post display page with context
    """
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)

    context = {
        'blog_post': blog_post,
    }

    return render(request, 'blog/blog_post.html', context)
