# Imports
# 3rd party:
from django.contrib import admin
# Internal:
from .models import Order, OrderLineItem
# -----------------------------------------------------------------------------


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Defines the order LineItem model in the admin
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Class defining the Order model for the admin
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number', 'date', 'delivery_cost', 'order_total',
        'grand_total', 'original_cart', 'stripe_pid',
    )

    fields = (
        'order_number', 'date', 'full_name', 'email',
        'phone_number', 'country', 'postcode', 'town_or_city',
        'address_line1', 'address_line2', 'county', 'delivery_cost',
        'order_total', 'grand_total', 'original_cart', 'stripe_pid',
    )

    list_display = (
        'order_number', 'date', 'full_name', 'order_total',
        'delivery_cost', 'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
