# Imports
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from reviews.models import Review
# Internal:
from .models import Product, Category
from .forms import ProductForm
from wishlist.models import Wishlist
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
                messages.error(request, 'Please input search parameters')
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
    in_wishlist = Wishlist.objects.filter(
        product=product, owner=request.user.id
    )

    context = {
        'product': product,
        'in_wishlist': in_wishlist
        }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    View for adding products to the database
        Arguments: request (object): The Http request
        Returns: Render add product page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry this feature is for store owners only.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.info(request, 'Product added to shop')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Could not add product. Please double-check the form.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    View for editing product details
        Arguments:
            request (object): The Http request
            product_id: ID of product being changed
        Returns:
            Render the edit product page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry this feature is for store owners only.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'New product details have been saved')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Could not make the desired changes. '
                'Please doublecheck the form.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You selected {product.name} for editing')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    View for deleting product details
        Arguments:
            request (object): The Http request
            product_id: ID of product being removed
        Returns:
            Redirect to products page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry this feature is for store owners only.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.info(request, 'Product removed successfully')
    return redirect(reverse('products'))
