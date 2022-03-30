# Imports
# 3rd party:
from django.shortcuts import render
# Internal
from products.models import Product
# -----------------------------------------------------------------------------


def index(request):
    """
    View to render the index page.
        Arguments: request (object): HTTP request object
        Returns: render index page
    """
    top_products = Product.objects.all().order_by('-rating')[:10]

    context = {
        'top_products': top_products,
    }
    return render(request, 'home/index.html', context)
