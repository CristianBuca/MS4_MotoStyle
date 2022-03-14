# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404
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


def product_detail(request):
    """
    View to render the product detail page
        Arguments:
            request (object): HTTP request object
            product_id: ID of product being viewed
        Returns: render product display page with context
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        }

    return render(request, 'products/product_detail.html', context)
