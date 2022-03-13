# Imports
# 3rd party:
from django.contrib import admin

# Internal:
from .models import Product, Category
# -----------------------------------------------------------------------------


class ProductAdmin(admin.ModelAdmin):
    """
    Class defining the products model in admin page
    """
    list_display = (
        'name', 'category', 'price', 'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Class defining the category model in admin page
    """
    list_display = (
        'name', 'friendly_name',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
