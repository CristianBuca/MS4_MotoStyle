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
    in_wishlist = Wishlist.objects.filter(
        product=product, owner=request.user.id
    )
    prod_reviews = Review.objects.filter(object_pk=product_id)
    rating = product.rating
    new_rating = update_rating(prod_reviews, rating)
    Product.objects.filter(pk=product_id).update(new_rating=new_rating)

    context = {
        'product': product,
        'in_wishlist': in_wishlist
        }

    return render(request, 'products/product_detail.html', context)


# Credit to Paul Meeneghan - LoveRugby project
# https://github.com/pmeeny/CI-MS4-LoveRugby
def update_rating(prod_reviews, rating):
    """
    Updates the rating of a product when a new review is posted
        Arguments: 
            prod_reviews: The reviews for the specific product
            rating: default product rating
        Returns: new rating
    """
    number_of_reviews = 0
    review_ratings = 0
    new_rating = 0
    for review in prod_reviews:
        number_of_reviews = number_of_reviews + 1
        review_ratings = review_ratings + review.rating

    if number_of_reviews > 0:
        if rating:
            average_rating = round((review_ratings / number_of_reviews), 1)
            new_rating = (float(rating) + float(average_rating)) / 2
        else:
            new_rating = round((review_ratings / number_of_reviews), 1)
        return new_rating
    else:
        return new_rating


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
            messages.success(request, 'Product added to shop')
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
    messages.success(request, 'Product removed successfully')
    return redirect(reverse('products'))
