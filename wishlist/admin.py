from django.contrib import admin

from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    """
    Admin class for the Wishlist model.
    """
    list_display = (
        'owner',
    )
    search_fields = (
        'owner',
    )
    list_filter = (
        'owner',
    )
    list_per_page = 20


admin.site.register(Wishlist, WishlistAdmin)
