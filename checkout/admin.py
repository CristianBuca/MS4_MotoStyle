# Imports
# 3rd party:
from django.contrib import admin
# Internal:
from .models import Order, OrderLineItem
# -----------------------------------------------------------------------------


class OrderAdmin(admin.ModelAdmin):
