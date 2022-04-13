# Imports
# 3rd party:
from django.shortcuts import render
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
