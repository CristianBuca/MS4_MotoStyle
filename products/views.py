# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
# Internal:
from .models import Product, Category
from .forms import ProductForm
# -----------------------------------------------------------------------------


def products(request):
    """
    View to render the products page, handle sorting and search queries
        Arguments: request (object): The Http request
        Returns: render products page with context
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey == 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'selected_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View to render the product detail page
        Arguments:
            request (object): The Http request
            product_id: ID of product being viewed
        Returns: render product display page with context
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """
    View for adding products to the database
        Arguments: request (object): The Http request
        Returns: Render add product page
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added to shop')
            return redirect(reverse('add_product'))
        else:
            messages.error(
                request, 'Could not add product. Please double-check the form'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
