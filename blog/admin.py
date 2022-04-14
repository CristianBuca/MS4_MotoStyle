# Imports
# 3rd party:
from django.contrib import admin
# Internal:
from .models import BlogPost
# -----------------------------------------------------------------------------


class BlogAdmin(admin.ModelAdmin):
    """
    Class defining the BlogPost model in admin page
    """
    list_display = (
        'id', 'title', 'created_at', 'image', 'second_image', 'third_image',
        'fourth_image', 'fifth_image',
    )

    ordering = ('owner', 'created_at')

    search_fields = ('title',)


admin.site.register(BlogPost, BlogAdmin)
