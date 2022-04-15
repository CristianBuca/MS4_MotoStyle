# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Internal:
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm
# -----------------------------------------------------------------------------


def blog(request):
    """
    View to render the blog page
        Arguments: request (object): The Http request
        Returns: render blog page with context
    """

    blog = BlogPost.objects.all().order_by('-id')
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
    comments = Comment.objects.all().filter(
        blog_article=blog_post).order_by('-posted_at')

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog_article = blog_post
            comment.posted_by = request.user
            comment.save()
            messages.info(request, 'Your comment has been posted')
            return redirect(reverse('blog_post', args=[blog_post.id]))
        else:
            messages.error(request, 'Unable to post comment at this time!')
            return redirect(reverse('blog_post', args=[blog_post.id]))
    else:
        comment_form = CommentForm()

    context = {
        'blog_post': blog_post,
        'comment_form': comment_form,
        'comments': comments,
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
            return redirect(reverse('blog'))
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


@login_required
def delete_blog_post(request, blog_post_id):
    """
    View for deleting a blog post
        Arguments:
            request (object): The Http request
            product_id: ID of blog post being removed
        Returns:
            Redirect to blog page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry this feature is for store owners only.')
        return redirect(reverse('blog'))

    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    blog_post.delete()
    messages.info(request, 'Article removed successfully')
    return redirect(reverse('blog'))
