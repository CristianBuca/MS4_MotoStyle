# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
# Internal:
from .models import Product, Category
# -----------------------------------------------------------------------------


def products(request):
    """
    View to render the products page, handle sorting and search queries
        Arguments: request (object): HTTP request object
        Returns: render products page with context
    """
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please input search parameters")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | Q(category__name__icontains=query)
            )
            products = products.filter(queries)
    context = {
        'products': products,
        'search_term': query,
        'selected_categories': categories,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
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
