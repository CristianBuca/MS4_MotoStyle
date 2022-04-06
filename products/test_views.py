# Imports
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
# Internal
from products.models import Product
# -----------------------------------------------------------------------------


class TestProductsViews(TestCase):
    """
    Defines the views unit tests for the products app
    """
    def test_get_products(self):
        """
        Tests if products page is accessible with status code of 200
        Tests if products view renders products.html
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_products_empty_search(self):
        """
        Tests if toasts displays error message when no search param in query
        Tests if user is redirected to products page
        """
        response = self.client.get('/products/', {'q': ''})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(
            messages[0]), 'Please input search parameters'
        )
        self.assertRedirects(response, '/products/')

    def test_get_products_search_query(self):
        """
        Tests if search query filters products by search term
        and sends status code 200
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        response = self.client.get('/products/', {'q': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_get_product_detail(self):
        """
        Tests if product_detail page is accessible with status code of 200
        Tests if product_detail view renders product_detail.html
        """
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_user_get_add_product(self):
        """
        Tests if regular user is redirected to landing page when trying to
        access add_product page with status code of 302
        Tests the error message returned in the toast
        """
        user = User.objects.create_user(
            username='unit_test_user', password='unit_test_pass'
        )
        self.client.login(username='unit_test_user', password='unit_test_pass')
        response = self.client.get('/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertEqual(str(
            messages[0]), 'Sorry this feature is for store owners only.'
        )

    def test_superuser_get_add_product(self):
        """
        Tests if superuser can access add_product page with status code of 200
        Tests if add_product view renders add_product,html template
        """
        user = User.objects.create_superuser(
            username='unit_test_superuser', password='unit_test_pass'
        )
        self.client.login(
            username='unit_test_superuser', password='unit_test_pass'
        )
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_superuser_post_add_product(self):
        """
        Tests if superuser can add product
        Tests if superuser is redirected to the product page
        Tests if toast displays correct message
        """
        user = User.objects.create_superuser(
            username='unit_test_superuser', password='unit_test_pass'
        )
        self.client.login(
            username='unit_test_superuser', password='unit_test_pass'
        )
        response = self.client.post('/products/add/', {
            'name': 'Test Add Product',
            'price': '123.45',
            'description': 'Test Add Product Description',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(
            messages[0]), 'Product added to shop'
        )
        self.assertRedirects(response, '/products/1/')

    def test_user_get_edit_product(self):
        """
        Tests if regular user is redirected to landing page when trying to
        access edit_product page with status code of 302
        Tests the error message returned in the toast
        """
        user = User.objects.create_user(
            username='unit_test_user', password='unit_test_pass'
        )
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.client.login(username='unit_test_user', password='unit_test_pass')
        response = self.client.get('/products/edit/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertEqual(str(
            messages[0]), 'Sorry this feature is for store owners only.'
        )

    def test_superuser_get_edit_product(self):
        """
        Tests if superuser can access edit_product page with status code of 200
        Tests if toast displays correct info message
        Tests if edit_product view renders edit_product.html template
        """
        user = User.objects.create_superuser(
            username='unit_test_superuser', password='unit_test_pass'
        )
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.client.login(
            username='unit_test_superuser', password='unit_test_pass'
        )
        response = self.client.get('/products/edit/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
        self.assertEqual(str(
            messages[0]), f'You selected {product.name} for editing'
        )

    def test_superuser_post_edit_product(self):
        """
        Tests if superuser can edit a product
        Tests if superuser is redirected to the product page
        Tests if toast displays correct message
        """
        user = User.objects.create_superuser(
            username='unit_test_superuser', password='unit_test_pass'
        )
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.client.login(
            username='unit_test_superuser', password='unit_test_pass'
        )
        response = self.client.post(f'/products/edit/{product.id}/', {
            'name': 'Test Edit Product',
            'price': '453.21',
            'description': 'Test Edit Product Description',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(
            messages[0]), 'New product details have been saved'
        )
        self.assertRedirects(response, '/products/1/')

    def test_user_delete_product(self):
        """
        Tests if regular user is redirected to landing page when trying to
        access delete_product page with status code of 302
        Tests the error message returned in the toast
        """
        user = User.objects.create_user(
            username='unit_test_user', password='unit_test_pass'
        )
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.client.login(username='unit_test_user', password='unit_test_pass')
        response = self.client.get('/products/delete/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertEqual(str(
            messages[0]), 'Sorry this feature is for store owners only.'
        )

    def test_superuser_delete_product(self):
        """
        Tests if superuser can delete a product
        Tests if superuser is redirected to the product page
        Tests if toast displays correct message
        """
        user = User.objects.create_superuser(
            username='unit_test_superuser', password='unit_test_pass'
        )
        product = Product.objects.create(
            name='Test Product',
            price='123.45',
            description='Test Product Description',
        )
        self.client.login(
            username='unit_test_superuser', password='unit_test_pass'
        )
        response = self.client.get('/products/delete/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')
        self.assertEqual(str(
            messages[0]), 'Product removed successfully'
        )
