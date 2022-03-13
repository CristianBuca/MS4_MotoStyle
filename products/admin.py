# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Class defining the products model in admin page
    """
    list_display = (
        'name', 'category', 'price', 'image',
    )

    ordering = ('category',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
