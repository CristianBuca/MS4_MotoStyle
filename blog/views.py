# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Internal:
from .models import BlogPost
from .forms import BlogPostForm
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


@login_required
def add_blog_post(request):
    """
    View for adding a blog post to the database
        Arguments: request (object): The Http request
        Returns: render the add blog post page
    """
    if request.method == 'POST':
        blog_form = BlogPostForm(request.POST, request.FILES)
        if blog_form.is_valid():
            form_data = blog_form.save(commit=False)
            form_data.owner = request.user
            form_data.save()
            messages.info(request, 'Your article has been posted.')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Could not post your article. Please check the form.'
            )
    else:
        form = BlogPostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
