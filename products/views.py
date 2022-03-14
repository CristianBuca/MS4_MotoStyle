# Imports
# 3rd party:
from django.shortcuts import render
# Internal:
from .models import Product
# -----------------------------------------------------------------------------


def products(request):
    """
    View to render the products page, handle sorting and search queries
        Arguments: request (object): HTTP request object
        Returns: render products page with context
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
