# **Moto Style**

## **Fourth Milestone Project - Full Stack Frameworks With Django - Code Institute**

![Moto Style](/docs/design/logos.png)

![Responsive Design](/docs/responsive_design/responsive_design.jpg)

# Table of Contents

- **[Project Overview](#project-overview)**
- **[User Experience](#user-experience)**
- **[Strategy](#strategy)**
  * **[Project Goals](#project-goals)**
  * **[User Goals](#user-goals)**
- **[Scope](#scope)**
  * **[User Stories](#user-stories)**
- **[Structure](#structure)**
  * **[Code Structure](#code-structure)**
  * **[Database Structure](#database-structure)**
    + **[Conceptual Database Model](#conceptual-database-model)**
    + **[Physical Database Model](#physical-database-model)**
  * **[Feature requirements](#feature-requirements)**
- **[Skeleton](#skeleton)**
  * **[Wireframes](#wireframes)**
  * **[App Routes](#app-routes)**
- **[Surface](#surface)**
  * **[Design](#design)**
- * **[Features](#features)**
    + **[Landing Page](#landing-page)**
    + **[Registration Page](#registration-page)**
    + **[Login Page](#login-page)**
    + **[My Shelf - User Collection Page](#my-shelf---user-collection-page)**
    + **[Add to Shelf Page](#add-to-shelf-page)**
    + **[Change Stock Page](#change-stock-page)**
    + **[Profile Page](#profile-page)**
    + **[Superuser Management Page Page](#superuser-management-page-page)**
    + **[Navbar](#navbar)**
    + **[Footer](#footer)**
    + **[Floating Action Button](#floating-action-button)**
    + **[Custom Error Pages](#custom-error-pages)**
  * **[Technologies Used](#technologies-used)**
  * **[Testing](#testing)**
  * **[Bugs](#bugs)**
  * **[Deployment](#deployment)**
  * **[Credits](#credits)**
  * **[Acknowledgements](#acknowledgements)**
  * **[Disclaimer](#disclaimer)**

## **You can find the deployed website** [**HERE**]()

# **Project Overview**

MotoStyle is a Full Stack e-commerce project developed as the final Milestone for Code Institute. It was created with Django Framework, using python as back-end and PostgreSQL as it's database while media is stored using AWS S3 services.
Purpose of the site is to enable a store to build a database of goods, showcase them and sell them online using stripe as the payment processor. 
The store owner has access to full CRUD functionality over the database and users of the site have access to CRUD functionality in the blog app over the content they add to the site.


**Registration on the website is open so feel free to take advantage of it. Regardless, for testing purposes I have set up the following account:**
* _Standard user:_ **testuser**  _password:_ **Password1**

# **User Experience**

This feature-rich e-commerce portal gives users access everything they need to make their shopping experience as complete as possible. Users are able to browse the products using a variety of sorting methods and search options. Once a product catches their eye, users have the options to add it to their wishlist or to their cart and purchase them using a safe payment processor - stripe. 
The reviews system allows them to post a review and a rating for each product as well as read other user's reviews. Once their shopping is complete, users have the option visit the blog section where they can post or read articles related to the motorcycle industry and community, as well as interact with each other in the comment sections.

# **Strategy**

##  **Project Goals**

* Use PostgreSQL to store data,
* Use Python and Django Framework to manipulate and present the data to the end-user,
* Use AWS to host and deliver media.
* Offer full CRUD functionality over the database to the store owners,
* Offer a responsive and mobile-friendly experience to users,

## **User Goals**

* Create an account on the site,
* Add products to the shopping cart,
* Purchase the items stored in the shopping cart,
* View reviews and articles related to the store's products,
* Interact with other users via the comments section,

[Back to Top](#top-shelf)


# **Scope**

## **User Stories**

**New Users:** 

1. As a new user, I want to be able to create and register an account.
2. As a new user, I want to be able to login and access my account.
3. As a new user, I want to be able to logout.
4. As a new user, I want to browse the store's merchandise.
5. As a new user, I want to be able to search for specific products.
6. As a new user, I want to be able to browse by categories.
7. As a new user, I want to be able to order product lists by price, rating, category or name.
8. As a new user, I want to view individual product details.
10. As a new user, I want to select the different quantities and sizes for a product.
11. As a new user, I want to be able to add products to my shopping cart.
12. As a new user, I want to be able to add products to a list of interests(wishlist).
13. As a new user, I want to be able to view the total cost of my shopping cart while I browse.
14. As a new user, I want to access and view my shopping cart.
15. As a new user, I want to adjust and manage the products in my shopping cart.
16. As a new user, I want to be able to purchase the selected products by entering my payment information in a secure way.
17. As a new user, I want to view an order confirmation.
18. As a new user, I want to receive the order confirmation via e-mail also.

**Regular Users:**

19. As a regular user, I want to store my delivery information for easy future checkouts.
20. As a regular user, I want to view a record of my past orders.
21. As a regular user, I want to view and manage my wishlist.
22. As a regular user, I want to review, rate and read other user's reviews for the products on the site.
23. As a regular user, I want the ability to recover my password.
24. As a regular user, I want to view articles related to the store products and the community it caters to.
25. As a regular user I want to be able to post, edit or remove articles from the blog section.
26. As a regular user, I want to be able to comment on articles.

**Super Users:**

27. As a super user, I want to add content to the store.
28. As a super user, I want to edit existing content.
29. As a super user, I want to delete existing content.
30. As a super user, I want to access the administration portal.

**Site Owner:**

31. As a site owner, I want the site to be responsive.
32. As a site owner, I want to showcase my social media.
33. As a site owner, I want to provide feedback to the user based on their interactions with the site.
34. As a site owner, I want forms to be validated on the front-end for better user experience.
35. As a site owner, I want forms to be validated on the back-end in case front-end is bypassed or fails.


[Back to Top](#top-shelf)


# **Structure**

## **Code Structure**

Project is structured in separate apps, each app hosting the required files to run:

* moto_style :
    - asgi.py - It exposes the ASGI callable as a module-level variable named ``application``.
    - settings.py - Global settings for the project
    - urls.py - The `urlpatterns` list routes URLs to views. Connects all app routes to main project.
    - wsgi.py - It exposes the WSGI callable as a module-level variable named ``application``

* home app:
    - static/home folder:
        - js folder hosts the script for the image slider on the landing page
    - templates/home folder:
        - index.html - Template for the landing page. Extends base template
    - apps.py - Default Django generated app config file
    - urls.py - Routes used by the views for the home app
    - views.py - Defines all the views in the home app
    - test_views.py - Unit tests for the views in the home app

* products app:
    - fixtures folder - contains json format fixtures for the products that need to be loaded in the database
    - static/products folder:
        - js folder - hosts the scripts for form validation, image notification, select element and quantity buttons used by the templates in the products app
    - templates/products folder:
        - custom widget template
        - includes for the product sizes
        - add_product.html - Page for adding a product to the store
        - edit_product.html - Page for editing a product from the store
        - product_detail.html - Page for displaying individual products
        - products.html - Page for displaying multiple products based on query params
    - admin.py - Defines the models from the products app in the admin panel
    - apps.py - Default Django generated app config file
    - forms.py - Defines the forms used by the products app
    - models.py - Defines the models used by the products app
    - urls.py - Routes used by the views in the products app
    - views.py - Defines all the views in the products app
    - widgets.py - Modifies the default Django CustomClearableFileInput widget
    - test_forms.py - Unit tests for the forms in the products app
    - test_models.py - Unit tests for the models in the products app
    - test_views.py - Unit tests for the views in the products app

* profiles app:
    - templates/profiles folder:
        - profile.html - Page for displaying user profile page with delivery information and order history
    - apps.py - Default Django generated app config file
    - forms.py - Defines the forms used by the profiles app
    - models.py - Defines the models used by the profiles app
    - urls.py - Routes used by the views in the profiles app
    - views.py - Defines all the views in the profiles app
    - test_forms.py - Unit tests for the forms in the profiles app
    - test_models.py - Unit tests for the models in the profiles app
    - test_views.py - Unit tests for the views in the profiles app 

* cart app:
    - static/cart folder:
        - js folder - hosts the script for the quantity buttons
    - templates/cart folder:
        - cart.html - Page for displaying the users shopping cart
    - templatetags folder:
        - cart_tools.py - defines custom template tags used by the cart app
    - apps.py - Default Django generated app config file
    - contexts.py - Defines cart context to be accessible outside the cart app
    - urls.py - Routes used by the views in the cart app
    - views.py - Defines all the views in the cart app
    - test_views.py - Unit tests for the views in the cart app 
    
* checkout app:
    - static/checkout folder:
        - css folder - hosts all the css specific to the checkout app
        - js folder - hosts the script used by the stripe API
    - templates/checkout folder:
        - emails folder - hosts the templates for the automated emails
        - checkout.html - Page for displaying the checkout form
        - checkout_success.html - Page for displaying the checkout confirmation and order summary
    - admin.py - Defines the models from the checkout app in the admin panel
    - apps.py - Default Django generated app config file
    - forms.py - Defines the forms used by the checkout app
    - models.py - Defines the models used by the checkout app
    - signals.py - Handles signals on item change to update the order
    - urls.py - Routes used by the views in the checkout app
    - views.py - Defines all the views in the checkout app
    - webhooks.py - Defines the stripe webhook
    - webhook_handler.py - Defines how different stripe webhooks are handled by the app
    - test_forms.py - Unit tests for the forms in the checkout app
    - test_models.py - Unit tests for the models in the checkout app
    - test_views.py - Unit tests for the views in the checkout app

* blog app:
    - static/blog folder:
        - css folder - hosts all the css specific to the blog app
        - js folder - hosts the scripts for the image notification
    - templates/blog folder:
        - custom widget template
        - add_blog_post Page for adding a a post to the blog
        - edit_blog_post Page for editing a post from the blog
        - blog_post.html - Page for displaying individual posts
        - blog.html - Page for displaying all blog posts
    - admin.py - Defines the models from the blog app in the admin panel
    - apps.py - Default Django generated app config file
    - forms.py - Defines the forms used by the blog app
    - models.py - Defines the models used by the blog app
    - urls.py - Routes used by the views in the blog app
    - views.py - Defines all the views in the blog app
    - widgets.py - Modifies the default Django CustomClearableFileInput widget
    - test_forms.py - Unit tests for the forms in the blog app
    - test_models.py - Unit tests for the models in the blog app
    - test_views.py - Unit tests for the views in the blog app

* wishlist app:
    - templates/wishlist folder:
        - wishlist.html - Page for displaying the products on the user's wishlist
    - admin.py - Defines the models from the wishlist app in the admin panel
    - apps.py - Default Django generated app config file
    - models.py - Defines the models used by the wishlist app
    - urls.py - Routes used by the views in the wishlist app
    - views.py - Defines all the views in the wishlist app
    - test_views.py - Unit tests for the views in the wishlist app

* static folder:
    - css folder: holds the project's global css
    - js folder: holds the scrips used globally

* templates folder:
    - allauth folder: hosts the 3rd party allauth app's templates that have been customized for this project
    - includes folder: hosts the includes used globally for the toasts, floating action button, main nav and mobile top header
    - reviews folder: hosts the 3rd party rated_reviews app's templates that have been customized for this project
    - 400.html, 403.html, 404.html, 500.html - custom error page
    - base.html - The base template for the project to be extended by each app's templates

* custom_storages.py - Defines the Media and Static storage locations for S3Boto3

* manage.py - Default Django generated command-line utility for administrative tasks.

* requirements.txt - contains information on python dependencies used for this app.

[Back to Top](#top-shelf)


## **Database Structure**

MotoStyle makes use of relational PostgreSQL for production environment and SQLite for development environment.

### **Conceptual Database Model**

Database concept was created using [QuickDBD](https://www.quickdatabasediagrams.com).

<details>
  <summary> (Expand) Conceptual Database Structure.</summary>

![Conceptual Database](/docs/database/conceptual_database.png)
</details>

### **Physical Database Model**

Database schema was generated with the Django extension [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html#selecting-a-library)

<details>
  <summary> (Expand) Physical Database Structure.</summary>

![items Collection](/docs/database/physical_database_schema.png)
</details>

### **Database Models**

Models used by this project are defined for each individual app in the `models.py` modules.

* **User model fields:**
Is imported from Allauth library.

    - id int pk
    - date_joined DateTimeField
    - email EmailField
    - username CharField
    - first_name CharField
    - last_name CharField
    - is_active BooleanField
    - is_staff BooleanField
    - is_superuser BooleanField
    - last_login DateTimeField
    - password CharField

* **User Profile model fields:**
Defined in the profiles app.

    - id int pk
    - user OneToOneField FK >- User.id
    - default_full_name  CharField(50)
    - default_email EmailField(254)
    - default_phone_number CharField(20)
    - default_address_line1 CharField(80)
    - default_address_line2 CharField(80)
    - default_postcode CharField(20)
    - default_town_or_city CharField(40)
    - default_area CharField(80)
    - default_country CountryField(2)

* **Category model fields:**
Defined in the products app.

    - id int pk
    - name CharField(254)
    - friendly_name CharField(254)
    - description TextField
    - image ImageField
    - image_url URLField(1024)

* **Product model fields:**
Defined in the products app.

    - id int pk
    - category ForeignKey FK >- Category.id
    - sku CharField(254)
    - name CharField(254)
    - description TestField
    - price DecimalField
    - rating DecimalField
    - image_url URLField(1024)
    - image ImageField
    - has_sizes BooleanField

* **Wishlist model fields:**
Defined in the wishlist app.

    - id int pk
    - owner ForeignKey FK >- User.id
    - product ForeignKey FK >- Product.id

* **Review model fields:**
Imported from Rated Reviews library.

    - id int pk
    - content_type ForeignKey FK >- ContentType.id
    - site ForeignKey FK >- Site.id
    - user ForeignKey FK >- User.id
    - comment TextField
    - ip_address GenericIPAddressField
    - is_public BooleanField
    - object_pk TextField
    - rating PositiveSmallIntegerField
    - submit_date DateTimeField
    - weight PositiveSmallIntegerField

* **OrderLineItem model fields:**
Defined in the checkout app.

    - id int pk
    - order int FK >- Order.id
    - product int FK >- Product.id
    - product_size CharField(2)
    - quantity int
    - lineitem_total DecimalField

* **Oder model fields:**
Defined in the checkout app.

    - id int pk
    - user_profile ForeignKey FK >- UserProfile.id
    - order_number CharField(32)
    - full_name CharField(254)
    - email EmailField(254)
    - phone_number CharField(20)
    - address_line1 CharField(80)
    - address_line2 (CharField(80)
    - postcode CharField(20)
    - town_or_city CharField(40)
    - area CharField(80)
    - country CountryField(2)
    - date DateTimeField
    - delivery_cost DecimalField
    - order_total DecimalField
    - grand_total DecimalField
    - original_cart TestField
    - stripe_pid CharField(254)

* **BlogPost model fields:**
Defined in the blog app.

    - id int pk
    - owner ForeignKey FK >- User.id
    - title CharField(254)
    - content TextField
    - image ImageField
    - image_url URLField(1024)
    - second_image ImageField
    - second_image_url URLField(1024)
    - third_image ImageField
    - third_image_url URLField(1024)
    - fourth_image ImageField
    - fourth_image_url URLField(1024)
    - fifth_image ImageField
    - fifth_image_url URLField(1024)
    - created_at DateTimeField

* **Comment model fields:**
Defined in the blog app.

    - id int pk
    - blog_article ForeignKey FK >- BlogPost.id
    - poste_by ForeignKey FK >- User.id
    - comment_body TextField(200)
    - posted_at DateTimeField

[Back to Top](#top-shelf)


## **Feature requirements**

* Responsive app for all device sizes.
* Collapsible Navigation bar on small devices.
* Footer with social media links.
* Landing Page showcasing (Read) items from the database.
* Registration Page with form validation.
* Login Page with form validation.
* Logout functionality with confirmation dialog.
* Search feature for products in the store.
* Sorting feature for products in the store by category, name, rating, price.
* Page where superusers can add products (Create entries) in the database.
* Administration Page where superusers can edit product details (Update entries) from the database.
* Superuser access to Delete feature with confirmation dialog for products in the database.
* Profile Page where users can Update personal details and view order history.
* Shopping cart where users can add products and is adjustable before checkout.
* Checkout feature secured by a safe payment provider [Stripe](https://stripe.com/gb).
* User access to wishlist feature where they can save favorite products for later purchase.
* User access to post reviews (Create entries) for products in the store.
* User access to post blog articles (Create entries) in the database.
* User access to edit blog articles (Update entries) in the database.
* User access to Delete feature with confirmation dialog for blog articles.
* User access to post comments (Create entries) in the database for blog articles.
* Notification system (message toast) to provide users with feedback to their interactions with the site.
* Administration panel for store owner with full CRUD control over the database.

[Back to Top](#top-shelf)

# **Skeleton**

## **Wireframes**

<details>
  <summary> (Expand) Landing Page Wireframes.</summary>

![Landing Page Wireframes](docs/wireframes/landing_page.png)
</details>

<details>
  <summary> (Expand) Registration Page Wireframes.</summary>

![Registration Page Wireframes](docs/wireframes/registration_view.png)
</details>

<details>
  <summary> (Expand) Login Page Wireframes.</summary>

![Login Page Wireframes](docs/wireframes/login_view.png)
</details>

<details>
  <summary> (Expand) Products Page Wireframes.</summary>

![Products Page Wireframes](docs/wireframes/products_view.png)
</details>

<details>
  <summary> (Expand) Product Details Page Wireframes.</summary>

![Product Details Page Wireframes](docs/wireframes/product_detail_view.png)
</details>

<details>
  <summary> (Expand) Add product to Database Page Wireframes.</summary>

![Add product to Database Page Wireframes](docs/wireframes/add_product_view.png)
</details>

<details>
  <summary> (Expand) Update product from the Database Page Wireframes.</summary>

![Update product from Database Page Wireframes](docs/wireframes/edit_product_view.png)
</details>

<details>
  <summary> (Expand) Profile Page Wireframes.</summary>

![Profile Page Wireframes](docs/wireframes/profile_view.png)
</details>

<details>
  <summary> (Expand) Wishlist Page Wireframes.</summary>

![Wishlist Page Wireframes](docs/wireframes/wishlist_view.png)
</details>

<details>
  <summary> (Expand) Shopping Cart Page Wireframes.</summary>

![Shopping Cart Page Wireframes](docs/wireframes/shopping_cart_view.png)
</details>

<details>
  <summary> (Expand) Checkout Page Wireframes.</summary>

![Checkout Page Wireframes](docs/wireframes/checkout_view.png)
</details>

<details>
  <summary> (Expand) Checkout Success Page Wireframes.</summary>

![Checkout Page Wireframes](docs/wireframes/checkout_success_view.png)
</details>

<details>
  <summary> (Expand) Blog Page Wireframes.</summary>

![Blog Page Wireframes](docs/wireframes/blog_view.png)
</details>

<details>
  <summary> (Expand) Blog Post Page Wireframes.</summary>

![Blog Post Page Wireframes](docs/wireframes/blog_post_view.png)
</details>

<details>
  <summary> (Expand) Add Blog Post Page Wireframes.</summary>

![Add Blog Page Wireframes](docs/wireframes/add_blog_post_view.png)
</details>

<details>
  <summary> (Expand) Update Blog Page Wireframes.</summary>

![Update Blog Page Wireframes](docs/wireframes/edit_blog_post_view.png)
</details>

[Back to Top](#top-shelf)


## **Project Routes**

**Home Route**
* Accessible from the Navbar Logo.
* Django path: `/`, view name: `home`.

**Registration Route**
* Accessible when logged out from the Account dropdown -> Register link in the top header navigation.
* Redirects to home page if already logged in.
* Django path: `/accounts/signup/`, view name: `account_signup`.

**Login Route**
* Accessible when logged out from the Account dropdown, -> Login link in the top header navigation.
* Redirects to home page if already logged in.
* Django path: `/accounts/login/`, view name: `account_login`.

**Products Route**
* Accessible from any of the category selections, filter or search queries.
* Django path: `/products/`, view name: `products`.

**Product Detail Route**
* Accessible by clicking on the product card displayed in `products`.
* Django path: `/products/<int:product_id>/`, view name: `products_detail`.

**Add Product Route**
* Accessible only by superusers by expanding the Floating Action Button (FAB) in the bottom right corner and selecting the second button with the "+" icon.
* Redirects to home page and displays and error message if not superuser.
* Redirects to login page if not logged in.
* Django path: `/products/add/`, view name: `add_product`.

**Update Product Route**
* Accessible only by superusers by clicking the button with a pencil icon on any of the product presentation cards or the product detail page.
* Redirects to home page and displays and error message if not superuser.
* Redirects to login page if not logged in.
* Django path: `/products/edit/<int:product_id>/`, view name: `edit_product`.

**Delete Product Route**
* Accessible only by superusers by clicking the button with a rubbish bin icon on any of the product presentation cards or the product detail page.
* Redirects to home page and displays and error message if not superuser.
* Redirects to login page if not logged in.
* Django path: `/products/delete/<int:product_id>/`, view name: `delete_product`.

**Profile Route**
* Accessible when logged in from the Account dropdown -> Profile link in the top header navigation.
* Redirects to login page if not logged in.
* Django path: `/profile/`, view name: `profile`.

**Order History Route**
* Accessible when logged in from the Profile page by clicking on the order number.
* Redirects to login page if not logged in.
* Django path: `/profile/order_history/<order_number>`, view name: `order history`.

**Wishlist Route**
* Accessible when logged in from the Account dropdown -> Wishlist link in the top header navigation.
* Redirects to login page if not logged in.
* Django path: `/wishlist/`, view name: `view_wishlist`.

**Wishlist Add Route**
* Accessible when logged in by clicking the Add to wishlist link on the product detail page.
* Redirects to login page if not logged in.
* Django path: `/wishlist/add/<product_id>/`, view name: `add_to_wishlist`.

**Wishlist Remove Route**
* Accessible when logged in by clicking the Remove from wishlist link on the product detail page.
* Redirects to login page if not logged in.
* Django path: `/wishlist/remove/<product_id>/`, view name: `remove_from_wishlist`.

**Cart Route**
* Accessible by clicking on the cart link with a shopping cart icon in the top header navigation.
* Django path: `/cart/`, view name: `view_cart`.

**Add to Cart Route**
* Accessible by clicking the add to cart button on the product detail page.
* Django path: `/cart/add/<item_id>/`, view name: `add_to_cart`.

**Update Cart Route**
* Accessible by clicking Update Quantity button for each product on the shopping cart page.
* Django path: `/cart/adjust/<item_id>/`, view name: `adjust_cart`.

**Remove from Cart Route**
* Accessible by clicking the Remove button for each product on the shopping cart page.
* Django path: `/cart/remove/<item_id>/`, view name `remove_from_cart`.

**Checkout Route**
* Accessible by clicking the Secure Checkout button on the shopping cart page or the toast success message.
* Django path: `/checkout/`, view name: `checkout`.

**Checkout Success**
* Presented to the user after clicking Complete Checkout button on the checkout page and checkout form is validated.
* Django path: `/checkout/checkout_success/<order_number>`, view name: `checkout_success`.

**Cache Checkout Data Route**
* Used internally by the checkout app and not accessible by users.
* Django path: `/checkout/cache_checkout_data/`, view name: `cache_checkout_data`.

**Webhook Route**
* Used by the stripe API and not accessible by users.
* Django path: `/checkout/wh/`, view name: `webhook`.

**Blog Route**
* Accessible by clicking on the blog link in the main navigation menu.
* Django path: `/blog/`, view name: `blog`.

**Blog Post Route**
* Accessible by clicking the Read More button from the blog post previews in the accordion on the blog page.
* Django path: `/blog/<int:blog_post_id>/`, view name: `blog_post`.

**Add Blog Post Route**
* Accessible when logged in by clicking the Post Article button on the blog page.
* Redirects to login page if not logged in.
* Django path: `/blog/add/`, view name: `add_blog_post`.

**Update Blog Post Route**
* Accessible only by superusers or user that created the post.
* Redirect to blog page and displays an error if accessed without permission.
* Redirects to login page if not logged in.
* Django path: `/blog/edit/<int:blog_post_id>/`, view name: `edit_blog_post`.

**Delete Blog Post Route**
* Accessible only by superusers or user that created the post.
* Redirect to blog page and displays an error if accessed without permission.
* Redirects to login page if not logged in.
* Django path: `/blog/delete/<int:blog_post_id>/`, view name: `delete_blog_post`.

**Delete Comment Route**
* Accessible only by superusers or user that created the post.
* Redirect to blog page and displays an error if accessed without permission.
* Redirects to login page if not logged in.
* Django path: `/delete_comment/<int:comment_id>/`, view name: `delete_comment`.

Routes used by third party apps like [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) and [Rated Reviews](https://django-rated-reviews.readthedocs.io/en/stable/) can be found in their respective documentation on [Read the Docs](https://readthedocs.org)

[Back to Top](#top-shelf)

# **Surface**

## **Design**

The MotoStyle project was designed with a mobile-first concept focusing on delivering to the user a feature-rich e-commerce experience that is responsive and functional on any device size. 

![Design desktop](/docs/design/desktop_view.png)

<details>
  <summary> (Expand) Design tablet.</summary>

![Design tablet](/docs/design/tablet_view.png)
</details>

<details>
  <summary> (Expand) Design mobile.</summary>

![Design mobile](/docs/design/mobile_view.png)
</details>


**UI**

MotoStyle makes use of the [Bootstrap 5.1](https://getbootstrap.com) CSS Framework which is directed at responsive, mobile-first front-end web development.

Two identities were created to highlight responsiveness:

![Identity](/docs/design/identity.JPG)


**Typography**

As the app is using Bootstrap library it inherits a lot of it's fonts as fallback. For the main components I have opted to overwrite those fonts with Lexend font family which was created with the intent to reduce visual stress and so improve reading performance.

**Color Palette**

![Color Pallette](/docs/design/color_palette.JPG)


[Back to Top](#top-shelf)


# **Features**

This projects features are accessible to the user based on their account permissions.
| Nav Link                  | Not logged in     | Logged in as user | Logged in as admin |
| ---                       | :---:             | :---:             | :---:     |
| Home                      |&#9989;            |&#9989;            |&#9989;    |
| Register                  |&#9989;            |&#10060;           |&#10060;   |
| Log in                    |&#9989;            |&#10060;           |&#10060;   |
| Log out                   |&#10060;           |&#9989;            |&#9989;    |    
| Profile                   |&#10060;           |&#9989;            |&#9989;    |    
| Order History             |&#10060;           |&#9989;            |&#9989;    |    
| Wishlist                  |&#10060;           |&#9989;            |&#9989;    |    
| Add to wishlist           |&#10060;           |&#9989;            |&#9989;    |    
| Remove from wishlist      |&#10060;           |&#9989;            |&#9989;    |    
| Products                  |&#9989;            |&#9989;            |&#9989;    |    
| Product Detail            |&#9989;            |&#9989;            |&#9989;    |    
| Product Detail (Review)   |&#10060;           |&#9989;            |&#9989;    |    
| Product Add               |&#10060;           |&#10060;           |&#9989;    |    
| Product Update            |&#10060;           |&#10060;           |&#9989;    |    
| Product Delete            |&#10060;           |&#10060;           |&#9989;    |    
| Blog                      |&#9989;            |&#9989;            |&#9989;    |    
| Blog Post                 |&#9989;            |&#9989;            |&#9989;    |    
| Blog Post (Comment)       |&#10060;           |&#9989;            |&#9989;    |
| Blog Post (Comment Delete)|&#10060;           |&#10060; (except created by)          |&#9989;    |      
| Blog Post Add             |&#10060;           |&#9989;            |&#9989;    |    
| Blog Post Update          |&#10060;           |&#10060; (except created by)          |&#9989;    |    
| Blog Post Delete          |&#10060;           |&#10060; (except created by)          |&#9989;    |    
| Cart                      |&#9989;            |&#9989;            |&#9989;    |    
| Checkout                  |&#9989;            |&#9989;            |&#9989;    |    
| Checkout success          |&#9989;            |&#9989;            |&#9989;    |
| Administration Panel      |&#10060;           |&#10060;           |&#9989;    | 

[Back to Top](#top-shelf)


### **Landing Page**

The Landing Page features the hero image and the search feature at the top of the page which users are able to take advantage of and search the database for a specific product. Main content of the page is comprised of a slider featuring the highest rated products in the store. The slider's width is responsive to the user's device size.

*User stories solved by this feature:*

* 4 - As a new user, I want to browse the store's merchandise.
* 5 - As a new user, I want to be able to search for specific products.
* 31 - As a site owner, I want the site to be responsive.

<details>
  <summary> (Expand) Landing Page on mobile, tablet and desktop view.</summary>

![Landing Page on mobile](/docs/features/landing_mobile.jpg)

![Landing Page on tablet](/docs/features/landing_tablet.jpg)

![Landing Page on desktop](/docs/features/landing_desktop.jpg)
</details>


### **Registration Feature**

Registration page is comprised of the registration form which is used to CREATE an user entry in the database User model for the Allauth app. The form is validated on the front-end by a custom JQuery script as well as on the back-end, providing feedback to the user when validation errors occur.

*User stories solved by this feature:*

* 1 - As a new user, I want to be able to create and register an account.
* 33 - As a site owner, I want to provide feedback to the user based on their interactions with the site.
* 34 - As a site owner, I want forms to be validated on the front-end for better user experience.
* 35 - As a site owner, I want forms to be validated on the back-end in case front-end is bypassed or fails.

<details>
  <summary> (Expand) Registration Page on mobile, tablet and desktop view.</summary>

![Registration Page on mobile](/docs/features/registration_mobile.jpg)

![Registration Page on tablet](/docs/features/registration_tablet.jpg)

![Registration Page on desktop](/docs/features/registration_desktop.jpg)
</details>

[Back to Top](#top-shelf)


### **Login Feature**

Login page is comprised of the login form which is used to READ an user entry from the database User model for the Allauth app. The form is validated on the back-end, providing feedback to the user input does not match the database entry. The login form hosts a "Forgot Password?" link that will allow the user to reset their password.


*User stories solved by this feature:*

* 2 - As a new user, I want to be able to login and access my account.
* 3 - As a new user, I want to be able to logout.
* 23 - As a regular user, I want the ability to recover my password.
* 33 - As a site owner, I want to provide feedback to the user based on their interactions with the site.
* 35 - As a site owner, I want forms to be validated on the back-end in case front-end is bypassed or fails.


<details>
  <summary> (Expand) Login Page on mobile, tablet and desktop view.</summary>

![Login Page mobile](/docs/features/login_mobile.jpg)

![Login Page tablet](/docs/features/login_tablet.jpg)

![Login Page desktop](/docs/features/login_desktop.jpg)
</details>


### **User Profile Feature**

The Profile Page enables users to store and update their delivery information for future checkouts and provides a order history list. Clicking on the order numbers in this list will provide the user a detailed order record.

*User stories solved by this feature:*

* 19 - As a regular user, I want to store my delivery information for easy future checkouts.
* 20 - As a regular user, I want to view a record of my past orders.

<details>
  <summary> (Expand) Profile Page on mobile, tablet and desktop view.</summary>

![Profile Page mobile](/docs/features/profile_mobile.jpg)

![Profile Page tablet](/docs/features/profile_tablet.jpg)

![Profile Page desktop](/docs/features/profile_desktop.jpg)
</details>

[Back to Top](#top-shelf)


### **Products Display Feature**

This feature provides the user with the ability to view all products, narrow down results by category/categories and sort them by their attributes. Clicking on a specific item will bring the user to the product's detail page where they are able to view detailed information, add the product their wishlist, read other user's reviews or rate and review the product themselves. After selecting their desired size and quantity the user is able to add the product to their shopping cart for later purchase.

*User stories solved by this feature:*

* 4 - As a new user, I want to browse the store's merchandise.
* 6 - As a new user, I want to be able to browse by categories.
* 7 - As a new user, I want to be able to order product lists by price, rating, category or name.
* 8 - As a new user, I want to view individual product details.
* 9 - As a new user, I want to select the different quantities and sizes for a product.
* 10 - As a new user, I want to be able to add products to my shopping cart.
* 11 - As a new user, I want to be able to add products to a list of interests(wishlist).
* 22 - As a regular user, I want to review, rate and read other user's reviews for the products on the site.

<details>
  <summary> (Expand) Products Feature on mobile, tablet and desktop view.</summary>

![Products Page mobile](/docs/features/products_mobile.jpg)

![Products Page tablet](/docs/features/products_tablet.jpg)

![Products Page desktop](/docs/features/products_desktop.jpg)
</details>


### **Product Management Feature**

Product management is accessible only to superusers. Adding a product from the Floating Action Button will bring up the Add Product Form and will CREATE a product entry in the database. Clicking the edit button on product cards or product details page will bring up the UPDATE Product Form. Clicking on the DELETE button on the product cards or product details page will trigger a confirmation modal for deletion. All forms are validated both on front-end and back-end to reduce risk of user error and maintain integrity of the store.

*User stories solved by this feature:*

* 27 - As a super user, I want to add content to the store.
* 28 - As a super user, I want to edit existing content.
* 29 - As a super user, I want to delete existing content.
* 34 - As a site owner, I want forms to be validated on the front-end for better user experience.
* 35 - As a site owner, I want forms to be validated on the back-end in case front-end is bypassed or fails.

<details>
  <summary> (Expand) Product Management on mobile, tablet and desktop view.</summary>

![Product Delete mobile](/docs/features/product_management_mobile.jpg)

![Product Update tablet](/docs/features/product_management_tablet.jpg)

![Product Add desktop](/docs/features/product_management_desktop.jpg)
</details>

[Back to Top](#top-shelf)


### **Shopping Cart Feature**

The shopping cart is stored in the browser's session cookies and is constantly updated when the user adds different products to it. The user is able to access their shopping cart from the top navigation and be presented with all the items selected, and the order summary displaying cost breakdowns. From each product card the user is also able to adjust the quantity or remove the product from the cart altogether.

*User stories solved by this feature:*

* 13 - As a new user, I want to access and view my shopping cart.
* 14 - As a new user, I want to adjust and manage the products in my shopping cart.

<details>
  <summary> (Expand) Shopping Cart on mobile, tablet and desktop view.</summary>

![Shopping Cart mobile](/docs/features/cart_mobile.jpg)

![Shopping Cart tablet](/docs/features/cart_tablet.jpg)

![Shopping Cart desktop](/docs/features/cart_desktop.jpg)
</details>


### **Checkout Feature**

Checkout is accessed from the shopping cart page or from the cart preview in the messages toast by clicking the secure checkout button. The user is prompted with a delivery form. The form uses the delivery information stored on the profile page if it exists. The card payment element is provided and secured by stripe along with the backend validation for the card. The user is also able to see a list of the items being purchased along with the total cost. Once the delivery and payment information have been validated, the user is able to complete the order with the form button at the bottom of the page. Upon completion an order confirmation screen is displayed with the order details and a confirmation e-mail is sent to the user's e-mail address.

*User stories solved by this feature:*

* 15 - As a new user, I want to be able to purchase the selected products by entering my payment information in a secure way.
* 16 - As a new user, I want to view an order confirmation.
* 17 - As a new user, I want to receive the order confirmation via e-mail also.
* 35 - As a site owner, I want forms to be validated on the back-end in case front-end is bypassed or fails.

<details>
  <summary> (Expand) Checkout on mobile, tablet and desktop view.</summary>

![Checkout mobile](/docs/features/checkout_mobile.jpg)

![Checkout tablet](/docs/features/checkout_tablet.jpg)

![Checkout desktop](/docs/features/checkout_desktop.jpg)
</details>

[Back to Top](#top-shelf)


### **Blog Feature**

The blog is accessed through the blog link in the main navigation and presents the user an accordion with all the articles posted on the site ordered by the most recent first. Upon expanding each accordion link the user is able to view a presentation of the article with the main image associated, a snippet of the article truncated to the first 40 words, information on who posted it and the date it was posted on.
The read more button will take the user to the article page where they can view a a image slide for the article (up to 5 images can be uploaded for each article), read the content and interact with other users in the comment section.

*User stories solved by this feature:*

* 24 - As a regular user, I want to view articles related to the store products and the community it caters to.
* 26 - As a regular user, I want to be able to comment on articles.

<details>
  <summary> (Expand) Blog on mobile, tablet and desktop view.</summary>

![Blog mobile](/docs/features/blog_mobile.jpg)

![Blog tablet](/docs/features/blog_tablet.jpg)

![Blog desktop](/docs/features/blog_desktop.jpg)
</details>

### **Blog Management Feature**

CREATING a post is currently open to all registered users and can be achieved by clicking the post article button at the top of the blog accordion. Users that are not logged in are redirected to the login page. UPDATING and DELETING a post is only available to the user that CREATED the post or superusers and is achieved through the buttons on each blog post in the accordion.

*User stories solved by this feature:*

* 25 - As a regular user I want to be able to post, edit or remove articles from the blog section.
* 27 - As a super user, I want to add content to the store.
* 28 - As a super user, I want to edit existing content.
* 29 - As a super user, I want to delete existing content.
* 35 - As a site owner, I want forms to be validated on the back-end in case front-end is bypassed or fails.

<details>
  <summary> (Expand) Blog Management on mobile, tablet and desktop view.</summary>

![Blog Management mobile](/docs/features/blog_management_mobile.jpg)

![Blog Management tablet](/docs/features/blog_management_tablet.jpg)

![Blog Management desktop](/docs/features/blog_management_desktop.jpg)
</details>

[Back to Top](#top-shelf)


### **Wishlist Feature**

The wishlist feature allows the user to selected products of interest and save them in one place between sessions; being specific to the each user it requires for the user to be logged in. It is accessed from the Account -> Wishlist link in the top header navigation and features cards with product images, names, prices that link to the specific product detail page. The user is able to add products to this list by clicking the Add to Wishlist links on each of the product's details page. This link will change icon and become a Remove from Wishlist link based on the product's status in the user's wishlist. Removal from the wishlist is also possible in the wishlist itself.

*User stories solved by this feature:*

* 11 - As a new user, I want to be able to add products to a list of interests(wishlist).
* 21 - As a regular user, I want to view and manage my wishlist.

<details>
  <summary> (Expand) Wishlist on mobile, tablet and desktop view.</summary>

![Wishlist mobile](/docs/features/wishlist_mobile.jpg)

![Wishlist tablet](/docs/features/wishlist_tablet.jpg)

![Wishlist desktop](/docs/features/wishlist_desktop.jpg)
</details>

### **Navbar**

The navigation bar is sectioned in 2 main components: the top header navigation and the main navigation.
- The top header navigation houses the site's logo who's identity changes based on device width and links to the home page, the search bar and links to Account functionality and shopping cart.
The Account dropdown will change it's link options based on the user's login status while the shopping cart will reflect the total cost of the products in it.
- The main navigation is structured based on products categories and subcategories which will restructure the products page results based on the categories filtered. In addition the main nav offers a link to the blog section as well as options to order all products by price, rating or category.
The main navigation collapses on medium devices and smaller and the main navigation is accessible from the burger menu on the left hand side.

*User stories solved by this feature:*

* 4 - As a new user, I want to browse the store's merchandise.
* 5 - As a new user, I want to be able to search for specific products.
* 6 - As a new user, I want to be able to browse by categories.
* 7 - As a new user, I want to be able to order product lists by price, rating, category or name.
* 12 - As a new user, I want to be able to view the total cost of my shopping cart while I browse.
* 31 - As a site owner, I want the site to be responsive.

<details>
  <summary> (Expand) Navbar on mobile, tablet and desktop view.</summary>

![Navbar mobile](/docs/features/navbar_mobile.jpg)

![Navbar tablet](/docs/features/navbar_tablet.jpg)

![Navbar desktop](/docs/features/navbar_desktop.jpg)
</details>

[Back to Top](#top-shelf)


### **Floating Action Button**

The floating action button at the bottom right hand side corner of the page changes based on the user's permissions. 
- For regular users and anonymous guests the FAB improves their user interaction with the site by providing a easy way to go back to the top of the page which can be invaluable on mobile devices to prevent long scrolling.
- For superusers the FAB changes to an expandable menu which provides links to the form for adding products to the store, link the administration portal created by Django as well as a back to top functionality.

*User stories solved by this feature:*

* 27 - As a super user, I want to add products to the store.
* 30 - As a super user, I want to access the administration portal.

<details>
  <summary> (Expand) Floating Action Button </summary>

![Floating Action Button](/docs/features/fab.jpg)

![Floating Action Button Superuser](/docs/features/fab_superuser.jpg)
</details>

[Back to Top](#top-shelf)

### **Toast alert message system**

The toast alerts provide the user a lightweight notification system and was built with Bootstrap's Toasts component. Located under the shopping cart link in the top header navigation, pops up when the user performs certain actions on the site and is styled based on Django's message categorization system: success, warning, info and error. The most notable is the success notification which is displayed when the user adds a product to their cart. The toast will include the success and a small preview of their shopping cart with a link to checkout. All the errors from unauthorized actions are also displayed here with tailored details on the why the errors ocurred.

*User stories solved by this feature:*

* 12 - As a new user, I want to be able to view the total cost of my shopping cart while I browse.
* 13 - As a new user, I want to access and view my shopping cart.
* 33 - As a site owner, I want to provide feedback to the user based on their interactions with the site.

<details>
  <summary> (Expand) Toast Notifications </summary>

![Toast Success](/docs/features/toast_success.jpg)

![Toast Error](/docs/features/toast_error.jpg)

![Toast Info](/docs/features/toast_info.jpg)

![Toast warning](/docs/features/toast_warning.jpg)
</details>

### **Footer**

In the footer, the user can find links to the owner's social media.

*User stories solved by this feature:*

* 32 - As a site owner, I want to showcase my social media.

<details>
  <summary> (Expand) Footer on mobile, tablet and desktop view. </summary>

![Footer mobile](/docs/features/footer_mobile.jpg)

![Footer tablet](/docs/features/footer_tablet.jpg)

![Footer desktop](/docs/features/footer_desktop.jpg)
</details>

[Back to Top](#top-shelf)

### **Custom Error Pages**

The Error Pages are displayed in case an error occurs on client, server or database side. It provides the user with the ability to easily go back to their area of interest maintaining user engagement.
Each error page displays it's specific error in the title. The user can still use the app's navbar to navigate or click the big button in the middle of the page to return to the Landing Page.
The errors that have specific routes on backend are:

* 400 Bad Request,
* 403 Forbidden Request,
* 404 Not Found,
* 500 Internal Server Error

*User stories solved by this feature:*

* 33 - As a site owner, I want to provide feedback to the user based on their interactions with the site.

<details>
  <summary> (expand) Error Page</summary>

![Error Page](/docs/features/error.jpg)
</details>

## **Administration portal**

Django offers a great administration portal out of the box that offers superusers full CRUD functionality over the database. Superusers can access it by clicking on the admin portal link with a wrench and screwdriver icon in the floating action button.
Configuring each app in this portal is achieved by defining the admin classes in each of the app's admin.py module and registering them:

```python
class WishlistAdmin(admin.ModelAdmin):
    """
    Admin class for the Wishlist model.
    """
    list_display = (
        'owner', 'product',
    )
    search_fields = (
        'owner',
    )
    list_filter = (
        'owner',
    )
    list_per_page = 20


admin.site.register(Wishlist, WishlistAdmin)
```

*User stories solved by this feature:*

* 30 - As a super user, I want to access the administration portal.

<details>
  <summary> (expand) Administration Portal</summary>

![Admin Portal](/docs/features/admin_portal.jpg)
</details>

[Back to Top](#top-shelf)

## **Technologies Used**

* **[HTML5](https://html.spec.whatwg.org)**
* **[CSS 3](https://www.w3.org/Style/CSS/Overview.en.html)**
* **[JavaScript](https://www.javascript.com)**
* **[Python 3.9.6](https://www.python.org)**
* **[SQLite](https://www.sqlite.org/index.html)** Was used as relational database for development.
* **[PostgreSQL](https://www.postgresql.org)** Was used as relational database for production.
* **[AWS S3](https://aws.amazon.com)** Was used to store static and media files in production.
* **[Stripe](https://stripe.com/gb)** As payment processor for store purchases.
* **[JQuery 3.6.0](https://jquery.com)** Was used for dom manipulation.
* **[Django 3.2](https://www.djangoproject.com)** Was used as the main framework for the project.
* **[Bootstrap 5.1](https://getbootstrap.com)** The project's front-end framework.
* **[Github](https://github.com/)** For storing my repository and documentation.
* **[Heroku](https://www.heroku.com/home)** For storing my repository and deploying the project. 
* **[Github Desktop](https://desktop.github.com)** For managing synchronizations between local and cloud-stored repositories.
* **[Git](https://git-scm.com)** For version control.
* **[VSCode](https://code.visualstudio.com)** IDE for writing code.
* **[Balsamiq](https://balsamiq.com)** For designing the wireframes.
* **[Font Awesome](https://fontawesome.com)** Provided the icons for social media links.
* **[Google Fonts](https://fonts.google.com)** Lexend font family was used as default font for the web application.
* **[Optimizilla](https://imagecompressor.com)** To optimize images for web applications.
* **[Favicon.io](https://favicon.io)** For creating the favicon.
* **[AmIResponsive](http://ami.responsivedesign.is)** For the multi-device mockup.
* **[Markdown ToC](https://ecotrust-canada.github.io/markdown-toc/)** Used to generate the table of contents for Readme.md


## **Testing**

Documentation on all tests carried out is available in [TESTING.md](/TESTING.md)

## **Bugs**

Documentation on all bugs and solutions is available in [TESTING.md](/TESTING.md)

## **Deployment**

The website is hosted [Github](https://github.com) and deployed on [Heroku](https://www.heroku.com/home).It uses [PostgreSQL](https://www.postgresql.org) as it's database, [AWS S3](https://aws.amazon.com) as cloud storage for static and media files, and [Stripe](https://stripe.com/gb) for payment processing. 
To be able to deploy this project accounts need to be created on all sites except PostgreSQL.

[Back to Top](#top-shelf)


**Hosting Repository on Github:** 

1. Login into Github account,
2. Select the button marked "New" and create a new repository,
3. Open repository with favorite IDE.

**Steps to follow to clone this repository:**

1. Log into your [Github](https://github.com) account,
2. Select the [Repository](https://github.com/CristianBuca/MS3_TopShelf),
3. Click on the drop-down menu title **Code** on the top right of the repository file tree,
4. Copy the HTTPS address,
5. In your Git Bash Terminal type *"git clone"* then paste the address.
6. Install all python dependencies by running this command in the terminal: `pip install -r requirements.txt`

*Alternatively you can download the repository as ZIP or use [Github Desktop](https://desktop.github.com) to get the repository on you local machine*

**Setting up environment variables required for the project to run in development**

1. Create a env.py file in the projects root directory.
2. Add your personal variables from the accounts you created in the env.py file following this syntax:

```python
import os

os.environ.setdefault('DEVELOPMENT', 'TRUE') - activates debug mode. Remove when in production.
os.environ.setdefault('USE_AWS', 'TRUE') - remove to use local files.
os.environ.setdefault('SECRET_KEY', '<your django secret key>') - [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) 
os.environ.setdefault('AWS_ACCESS_KEY_ID', '<your AWS access key>')
os.environ.setdefault('AWS_SECRET_ACCESS_KEY', '<your AWS secret access key')
os.environ.setdefault('DATABASE_URL', '<your database url>') - remove to use local Django database
os.environ.setdefault('STRIPE_PUBLIC_KEY', '<your stripe public key>')
os.environ.setdefault('STRIPE_SECRET_KEY', '<your stripe secret key>')
os.environ.setdefault('STRIPE_WH_SECRET', '<your stripe webhook key>')
os.environ.setdefault('EMAIL_HOST_USER', '<your email host username>')
os.environ.setdefault('EMAIL_HOST_PASS', '<your email host password>')
```

**Deployment to Heroku:**

1. Create a Procfile in the root directory with contents `web:python app.py`,
2. Run `pip freeze > requirements.txt` in terminal,
3. Login into Heroku,
4. Click "Create new app",
5. Click "Resources" tab, search for postgres in the addons field and provision a PostgreSQL database for your project.
6. Click "Settings" and select "Reveal Config Vars",
7. The database address will be shown here under "DATABASE_URL".
8. Add the rest of the config vars used in env.py,
9. Click the "Deploy" tab  and as deployment method select GitHub,
10. Select the relevant repository with the help of the search field and click Connect,
11. Select "Deploy Brach",
12. After deployment is successful enable automatic deploys. 

![Deploy with Heroku](/docs/deployment/heroku.png)

[Back to Top](#top-shelf)

**Setting up AWS S3:**

1. Login into your AWS account.
2. Find S3 in services and select it.
3. Click the "Create bucket" button.
4. Give the bucket a name and select the region closest to you.
5. Under Object Ownership select "ACLs enabled" and "Bucket owner preferred.
6. Uncheck "Block all public access"  and acknowledge the change.
7. Create the bucket.
8. Select the bucket and under the "Properties" tab go to "Static website hosting" and enable it.
9. Select the "Permissions" tab and under Cross-origin resource sharing (CORS) add the following code:

```
[
{
"AllowedHeaders": [
"Authorization"
],
"AllowedMethods": [
"GET"
],
"AllowedOrigins": [
"*"
],
"ExposeHeaders": []
}
]
```
10. Select the "Bucket Policy" tab, copy the Bucket ARN to clipboard and click "Policy Generator".
11. Select type of policy: S3 Bucket policy, in Principal field add "*" and under Actions select "GetObject".
12. In the "Amazon Resource Name" field paste your ARN from step 10.
13. Click "Add Statement", then "Generate Policy" and copy the policy.
14. Go back to Bucket Policy, paste the new policy generated and at the end of the Resource key add "/*" then click Save.
15. Select "Edit" under Access control list (ACL) and enable list access for Everyone(public access).


**Setting up AWS IAM:**

1. Login into your AWS account.
2. Find IAM in services and select it.
3. Select "User groups" under Access management and click "Create group".
4. Enter the name of your group and create it.
5. Select "Policies" under Access management and click "Create policy".
6. Go to the "JSON" tab and click Import managed policy.
7. Search for "S3" and select "AmazonS3FullAccess" policy then click Import.
8. Get the bucket ARN from S3 (refer to Setting up AWS S3 step 10) and under the Resource key add a list with the ARN and the ARN followed by "/*".
9. Click Next, then Next:Review, enter a policy name and description and click "Create Policy".
10. Go back to Groups and select the group you created at step 4, go to "Permissions" tab and click "Add permissions".
11. Select "Attack policies", select the policy you just created and click "Attach policy".
12. Select "Users" under Access management and click "Add user".
13. Enter a user name and under "Select AWS credential type" select "Access key - Programmatic access".
14. Click "Next:Permissions" and add user to the group you created at step 4.
15. Click Next to the end and Create user.
16. !At the Success screen download the .csv file with the user's access key and save it. This will contain this users access key and secret access key which are used to authenticate from Django. Once passed through this process you can't download them again.
17. Copy those keys into our environment variables.


**Setting up Stripe:**

1. Login into your Stripe account.
2. Click on "Developers" and select "API keys".
3. Copy the public and secret keys into your environment variables.
4. Select "webhooks" and click "Add endpoint".
5. In "Endpoint URL" field enter your heroku deployment address followed "/checkout/wh/".
6. Under "Select events" select payment_intent.payment_failed and payment_intent.succeeded then click "Add endpoint".
7. Select the endpoint you added and click "Reveal" under Signing Secret.
8. Copy the signing secret in your environment "STRIPE_WH_SECRET" key.

[Back to Top](#top-shelf)


## **Credits**

This Project was created based on the Code Institute - Hello Django and Boutique Ado Project Lessons by [Chris Z](https://github.com/ckz8780).
There are inevitable similarities between this project and the ones in these lessons, more specifically:

**From Boutique Ado lessons I used:**

* Overall approach on building the project using Django,
* Structure of the apps and database,
* Stripe integration and webhook handling,
* JQuery script for quantity buttons,
* JQuery script for sorting element

**From Hello Django lessons I used:**

* Automated testing methods for forms, models and views.

### **Third party plugins and extensions:**

**JQuery form validation** was done using the [Jquery Validation Plugin](https://jqueryvalidation.org/documentation/).

**Django 3rd party libraries and extensions can be found in requirements.txt but the most notable are:**

* [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - for user authentication.
* [Django-Rated Reviews](https://django-rated-reviews.readthedocs.io/en/latest/) - for the review and rating features.


**Media**

* Hero Image from [Pexels](https://www.pexels.com/photo/person-riding-motorcycle-during-golden-hour-1416169/).
* All product images, and content from [J&S Accessories](https://jsaccessories.co.uk).
* Blog posts and images from [MCN](https://www.motorcyclenews.com). 


### **Code Institute colleagues who's work I followed for guidance:**

[Carla Buongiorno](https://github.com/CarlaBuongiorno/la_fraschetta).

[Paul Meeneghan](https://github.com/pmeeny/CI-MS4-LoveRugby).


## **Acknowledgements**

* Special thanks to my mentor Mo Shami for his suggestions and guidance.
* Special thanks to my brother for his feedback and suggestions and always having my back.
* My family for their encouragement and support.
* The Code Institute tutors that helped me when I was hitting walls.
* The Code Institute team for all the effort and energy they put into creating and curating the content for this programme.

## Disclaimer

_This project is for educational use only and was created as a Milestone Project for the Code Institute Module of Interactive Frontend Development_

Developed by Cristian Buca

[Back to Top](#top-shelf)

