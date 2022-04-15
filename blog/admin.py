# Imports
# 3rd party:
from django.contrib import admin
# Internal:
from .models import BlogPost, Comment
# -----------------------------------------------------------------------------


class BlogAdmin(admin.ModelAdmin):
    """
    Class defining the BlogPost model in admin page
    """
    list_display = (
        'id', 'owner', 'title', 'created_at', 'image', 'second_image',
        'third_image', 'fourth_image', 'fifth_image',
    )
    ordering = ('owner', 'created_at')
    search_fields = ('title', )
    list_filter = ('owner', )


class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for the Comment model.
    """
    list_display = (
        'posted_by', 'blog_article', 'posted_at'
    )
    ordering = ('posted_by', 'posted_at')
    search_fields = ('posted_by', 'blog_article')
    list_filter = ('posted_by', )


admin.site.register(BlogPost, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
