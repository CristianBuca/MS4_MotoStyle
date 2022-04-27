# Testing Documentation

![Responsive Design](/docs/design/responsive_design.jpg)

# Table of contents

- [Unit Testing:](#unit-testing)
- [HTML Validation](#html-validation)
- [CSS Validation](#css-validation)
- [WAVE Accessibility Validation](#wave-accessibility-validation)
- [Lighthouse Tests](#lighthouse-tests)
- [Javascript Validation](#javascript-validation)
- [Python Validation](#python-validation)
- [Physical Testing](#physical-testing)
- [Testing of User Stories](#testing-of-user-stories)
  * [New User Stories](#new-user-stories)
  * [Returning User Stories](#returning-user-stories)
  * [Super Users Stories](#super-users-stories)
  * [Site Owner Stories](#site-owner-stories)
- [Bugs](#bugs)



## **[Return to Readme.md](/README.md)**

## **You can find the deployed website** [**HERE**](https://ms4-motostyle.herokuapp.com)


# Unit Testing:

## Automated tests were written and carried out for each app. The tests are separated into test_forms, test_models and test_views modules.

**All tests pass with no Fails or Errors:**

![Unit tests](/docs/test_img/unit_tests/unit_tests.jpg)

**These tests cover 84% of the project's code excluding migrations and 3rd party apps.**

![Coverage Report](/docs/test_img/unit_tests/coverage_report.jpg)

[Back to Top](#testing-documentation)


# HTML Validation

## HTML validation was carried out with [W3 Validator](https://validator.w3.org).


<details>
  <summary> (expand) Landing Page HTML Validation found 0 errors:</summary>

![Landing Page HTML Validation](/docs/test_img/html_validator/html_valid_landing.png)

</details>

<details>
  <summary> (expand) Registration Page HTML Validation found 0 errors:</summary>

![Registration Page HTML Validation](/docs/test_img/html_validator/html_valid_register.png)

</details>

<details>
  <summary> (expand) Login Page HTML Validation found 0 errors:</summary>

![Login Page HTML Validation](/docs/test_img/html_validator/html_valid_login.png)

</details>

<details>
  <summary> (expand) Products Page HTML Validation found 0 errors:</summary>

![Products Page HTML Validation](/docs/test_img/html_validator/html_valid_products.png)

</details>

<details>
  <summary> (expand) Product Detail Page HTML Validation found 0 errors:</summary>

![Product Detail Page HTML Validation](/docs/test_img/html_validator/html_valid_product_detail.png)

</details>

<details>
  <summary> (expand) Add Product Page HTML Validation found 0 errors:</summary>

![Add Product Page HTML Validation](/docs/test_img/html_validator/html_valid_product_add.png)

</details>

<details>
  <summary> (expand) Update Product Page HTML Validation found 0 errors:</summary>

![Update Product Page HTML Validation](/docs/test_img/html_validator/html_valid_product_edit.png)

</details>

<details>
  <summary> (expand) Profile Page HTML Validation found 0 errors:</summary>

![Profile Page HTML Validation](/docs/test_img/html_validator/html_valid_profile.png)

</details>

<details>
  <summary> (expand) Wishlist Page HTML Validation found 0 errors:</summary>

![Wishlist Page HTML Validation](/docs/test_img/html_validator/html_valid_wishlist.png)

</details>

<details>
  <summary> (expand) Shopping Cart Page HTML Validation found 0 errors:</summary>

![Shopping Cart Page HTML Validation](/docs/test_img/html_validator/html_valid_cart.png)

</details>

<details>
  <summary> (expand) Checkout Page HTML Validation found 0 errors:</summary>

![Checkout Page HTML Validation](/docs/test_img/html_validator/html_valid_checkout.png)

</details>

<details>
  <summary> (expand) Checkout Success Page HTML Validation found 0 errors:</summary>

![Checkout Success Page HTML Validation](/docs/test_img/html_validator/html_valid_checkout_success.png)

</details>

<details>
  <summary> (expand) Blog Page HTML Validation found 0 errors:</summary>

![Blog Page HTML Validation](/docs/test_img/html_validator/html_valid_blog.png)

</details>

<details>
  <summary> (expand) Blog Post Page HTML Validation found 0 errors:</summary>

![Blog Post Page HTML Validation](/docs/test_img/html_validator/html_valid_blog_post.png)

</details>

<details>
  <summary> (expand) Add Blog Post Page HTML Validation found 0 errors:</summary>

![Add Blog Post Page HTML Validation](/docs/test_img/html_validator/html_valid_blog_add.png)

</details>

<details>
  <summary> (expand) Update Blog Post Page HTML Validation found 0 errors:</summary>

![Update Blog Post Page HTML Validation](/docs/test_img/html_validator/html_valid_blog_edit.png)

</details>

[Back to Top](#testing-documentation)


# CSS Validation

## CSS validation was carried out with [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).

<details>
  <summary> (expand) base.css Jigsaw Validation found 0 errors, 18 warnings due to vendor extensions:</summary>

![base.css CSS Validation](/docs/test_img/css_validator/css_valid_base.png)

</details>

<details>
  <summary> (expand) blog.css Jigsaw Validation found 0 errors:</summary>

![blog.css Validation](/docs/test_img/css_validator/css_valid_blog.png)

</details>

<details>
  <summary> (expand) checkout.css Jigsaw Validation found 0 errors, 1 warning due to vendor extension:</summary>

![checkout.css Validation](/docs/test_img/css_validator/css_valid_checkout.png)

</details>


# WAVE Accessibility Validation

## Accessibility Evaluation was carried out with [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org).

<details>
  <summary> (expand) Landing Page WAVE Validation found 0 errors:</summary>

![Landing Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_landing.jpg)

</details>

<details>
  <summary> (expand) Registration Page WAVE Validation found 0 errors:</summary>

![Registration Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_register.jpg)

</details>

<details>
  <summary> (expand) Login Page WAVE Validation found 0 errors:</summary>

![Login Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_login.jpg)

</details>

<details>
  <summary> (expand) Products Page WAVE Validation found 0 errors:</summary>

![Products Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_products.jpg)

</details>

<details>
  <summary> (expand) Product Detail Page WAVE Validation found 2 errors, 1 alert due to 3rd party Rated Reviews App form labels:</summary>

![Product Detail Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_product_detail.jpg)

</details>

<details>
  <summary> (expand) Add Product Page WAVE Validation found 0 errors, 1 alert due to Django widget form labels:</summary>

![Add Product Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_products_add.jpg)

</details>

<details>
  <summary> (expand) Update Page WAVE Validation found 0 errors, 1 alert due to Django widget form labels:</summary>

![Update Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_products_edit.jpg)

</details>

<details>
  <summary> (expand) Profile Page WAVE Validation found 0 errors:</summary>

![Profile Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_profile.jpg)

</details>

<details>
  <summary> (expand) Wishlist Page WAVE Validation found 0 errors:</summary>

![Wishlist Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_wishlist.jpg)

</details>

<details>
  <summary> (expand) Shopping Cart Page WAVE Validation found 0 errors:</summary>

![Shopping Cart Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_cart.jpg)

</details>

<details>
  <summary> (expand) Checkout Page WAVE Validation found 0 errors:</summary>

![Checkout Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_checkout.jpg)

</details>

<details>
  <summary> (expand) Checkout Success Page WAVE Validation found 0 errors:</summary>

![Checkout Success Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_checkout_success.jpg)

</details>

<details>
  <summary> (expand) Blog Page WAVE Validation found 0 errors:</summary>

![Blog Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_blog.jpg)

</details>

<details>
  <summary> (expand) Blog Post Page WAVE Validation found 0 errors:</summary>

![Blog Post Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_blog_post.jpg)

</details>

<details>
  <summary> (expand) Add Blog Post Page WAVE Validation found 0 errors, 4 alerts due to Django widget form labels:</summary>

![Add Blog Post Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_blog_add.jpg)

</details>

<details>
  <summary> (expand) Update Blog Post Page WAVE Validation found 0 errors, 6 alerts due to Django widget form labels:</summary>

![Update Blog Post Page WAVE Validation](/docs/test_img/wave_validator/wave_valid_blog_edit.jpg)

</details>

[Back to Top](#testing-documentation)


# Lighthouse Tests

## Performance Tests were carried out using Chrome Lighthouse DevTools.

<details>
  <summary> (expand) Landing Page Lighthouse Test:</summary>

![Landing Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_landing.jpg)

</details>

<details>
  <summary> (expand) Registration Page Lighthouse Test:</summary>

![Registration Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_register.jpg)

</details>

<details>
  <summary> (expand) Login Page Lighthouse Test:</summary>

![Login Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_login.jpg)

</details>

<details>
  <summary> (expand) Products Page - 1 category Lighthouse Test with images loading from AWS:</summary>

![Products - 1 category Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_products_category.jpg)

</details>

<details>
  <summary> (expand) Products Page - 96 products Lighthouse Test with images loading from AWS:</summary>

![Products Page - 96 products Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_products.jpg)

</details>

<details>
  <summary> (expand) Product Detail Page Lighthouse Test:</summary>

![Product Detail Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_product_detail.jpg)

</details>

<details>
  <summary> (expand) Add Product Page Lighthouse Test:</summary>

![Add Product Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_product_add.jpg)

</details>

<details>
  <summary> (expand) Update Product Page Lighthouse Test:</summary>

![Update Product Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_product_edit.jpg)

</details>

<details>
  <summary> (expand) Profile Page Lighthouse Test:</summary>

![Profile Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_profile.jpg)

</details>

<details>
  <summary> (expand) Wishlist Page Lighthouse Test:</summary>

![Wishlist Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_wishlist.jpg)

</details>

<details>
  <summary> (expand) Shopping Cart Page Lighthouse Test:</summary>

![Shopping Cart Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_cart.jpg)

</details>

<details>
  <summary> (expand) Checkout Page Lighthouse Test:</summary>

![Checkout Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_checkout.jpg)

</details>

<details>
  <summary> (expand) Checkout Success Page Lighthouse Test:</summary>

![Checkout Success Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_checkout_success.jpg)

</details>

<details>
  <summary> (expand) Blog Page Lighthouse Test:</summary>

![Blog Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_blog.jpg)

</details>

<details>
  <summary> (expand) Blog Post Page Lighthouse Test:</summary>

![Blog Post Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_blog_post.jpg)

</details>

<details>
  <summary> (expand) Add Blog Post Page Lighthouse Test:</summary>

![Add Blog Post Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_blog_add.jpg)

</details>

<details>
  <summary> (expand) Update Blog Post Page Lighthouse Test:</summary>

![Update Blog Post Page Lighthouse Test](/docs/test_img/lighthouse_tests/lighthouse_blog_edit.jpg)

</details>

[Back to Top](#testing-documentation)


# Javascript Validation

## JavaScript Code Tests were carried out with [JShint](https://jshint.com).

<details>
  <summary> (expand) /static/js/form_validation.js Script JSHint Test no errors:</summary>

![/static/js/form_validation Script JSHint Test](/docs/test_img/jshint_validator/jshint_valid_signup.png)

</details>

<details>
  <summary> (expand) Blog App image_notification.js Script JSHint Test no errors:</summary>

![Blog app image_notification Script JSHint Test](/docs/test_img/jshint_validator/jshint_valid_blog_image_notif.png)

</details>

<details>
  <summary> (expand) Cart App cart.js Script JSHint Test no errors:</summary>

![Cart App cart.js Script JSHint Test](/docs/test_img/jshint_validator/jshint_valid_cart.png)

</details>

<details>
  <summary> (expand) Products App form_validation.js Script JSHint Test no errors:</summary>

![Products App form_validation.js Script JSHint Test](/docs/test_img/jshint_validator/jshint_valid_products_form.png)

</details>

<details>
  <summary> (expand) Products App image_notification.js Script JSHint Test no errors:</summary>

![Products App image_notification.js Script JSHint Test](/docs/test_img/jshint_validator/jshint_valid_products_image_notif.png)

</details>

<details>
  <summary> (expand) Products App products.js Script JSHint Test no errors:</summary>

![Products App products.js Script JSHint Test](/docs/test_img/jshint_validator/jshint_valid_products.png)

</details>

<details>
  <summary> (expand) Products App quantity_buttons.js Script JSHint Test no errors:</summary>

![Products App quantity_buttons.js Script JSHint Test](/docs/test_img/jshint_validator/jshint_valid_products_quant_btns.png)

</details>

<details>
  <summary> (expand) Home App slider.js Script JSHint Test no errors:</summary>

![Home App slider.js Script JSHint Test](/docs/test_img/jshint_validator/jshint_valid_slider.png)

</details>

<details>
  <summary> (expand) Checkout App stripe.js Script JSHint Test no errors:</summary>

![Checkout App stripe.js Script JSHint Test](/docs/test_img/jshint_validator/jshint_valid_stripe.png)

</details>

[Back to Top](#testing-documentation)


# Python Validation

## Python Code Tests were carried out with [Pep8](http://pep8online.com) on all python modules and results are structured by app:


### Blog App:

<details>
  <summary> (expand) admin.py Pep8 found 0 errors:</summary>

![admin.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_blog_admin.png)

</details>

<details>
  <summary> (expand) apps.py Pep8 found 0 errors:</summary>

![apps.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_blog_apps.png)

</details>

<details>
  <summary> (expand) forms.py Pep8 found 0 errors:</summary>

![forms.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_blog_forms.png)

</details>

<details>
  <summary> (expand) models.py Pep8 found 0 errors:</summary>

![models.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_blog_models.png)

</details>

<details>
  <summary> (expand) urls.py Pep8 found 0 errors:</summary>

![urls.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_blog_urls.png)

</details>

<details>
  <summary> (expand) views.py Pep8 found 0 errors:</summary>

![views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_blog_views.png)

</details>

<details>
  <summary> (expand) widgets.py Pep8 found 0 errors:</summary>

![widgets.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_blog_widgets.png)

</details>


### Cart App:

<details>
  <summary> (expand) apps.py Pep8 found 0 errors:</summary>

![apps.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_cart_apps.png)

</details>

<details>
  <summary> (expand) contexts.py Pep8 found 0 errors:</summary>

![contexts.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_cart_contexts.png)

</details>

<details>
  <summary> (expand) test_views.py Pep8 found 0 errors:</summary>

![test_views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_cart_test_views.png)

</details>

<details>
  <summary> (expand) urls.py Pep8 found 0 errors:</summary>

![urls.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_cart_urls.png)

</details>

<details>
  <summary> (expand) views.py Pep8 found 0 errors:</summary>

![views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_cart_views.png)

</details>

[Back to Top](#testing-documentation)


### Checkout App:

<details>
  <summary> (expand) admin.py Pep8 found 0 errors:</summary>

![admin.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_admin.png)

</details>

<details>
  <summary> (expand) apps.py Pep8 found 0 errors:</summary>

![apps.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_apps.png)

</details>

<details>
  <summary> (expand) forms.py Pep8 found 0 errors:</summary>

![forms.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_forms.png)

</details>

<details>
  <summary> (expand) models.py Pep8 found 0 errors:</summary>

![models.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_models.png)

</details>

<details>
  <summary> (expand) signals.py Pep8 found 0 errors:</summary>

![signals.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_signals.png)

</details>

<details>
  <summary> (expand) test_forms.py Pep8 found 0 errors:</summary>

![test_forms.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_test_forms.png)

</details>

<details>
  <summary> (expand) test_models.py Pep8 found 0 errors:</summary>

![test_models.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_test_models.png)

</details>

<details>
  <summary> (expand) test_views.py Pep8 found 0 errors:</summary>

![test_views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_test_views.png)

</details>

<details>
  <summary> (expand) urls.py Pep8 found 0 errors:</summary>

![urls.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_urls.png)

</details>

<details>
  <summary> (expand) views.py Pep8 found 0 errors:</summary>

![views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_views.png)

</details>

<details>
  <summary> (expand) webhook_handler.py Pep8 found 0 errors:</summary>

![webhook_handler.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_webhook_handler.png)

</details>

<details>
  <summary> (expand) webhook_handler.py Pep8 found 0 errors:</summary>

![webhook_handler.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_checkout_webhook.png)

</details>


### Home App:

<details>
  <summary> (expand) apps.py Pep8 found 0 errors:</summary>

![apps.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_home_apps.png)

</details>

<details>
  <summary> (expand) test_views.py Pep8 found 0 errors:</summary>

![test_views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_home_test_views.png)

</details>

<details>
  <summary> (expand) urls.py Pep8 found 0 errors:</summary>

![urls.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_home_urls.png)

</details>

<details>
  <summary> (expand) views.py Pep8 found 0 errors:</summary>

![views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_home_views.png)

</details>

[Back to Top](#testing-documentation)


### Moto Style config modules:

<details>
  <summary> (expand) asgi.py Pep8 found 0 errors:</summary>

![asgi.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_moto_style_asgi.png)

</details>

<details>
  <summary> (expand) settings.py Pep8 found 0 errors:</summary>

![settings.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_moto_style_settings.png)

</details>

<details>
  <summary> (expand) urls.py Pep8 found 0 errors:</summary>

![urls.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_moto_style_urls.png)

</details>

<details>
  <summary> (expand) wsgi.py Pep8 found 0 errors:</summary>

![wsgi.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_moto_style_wsgi.png)

</details>


### Products App:

<details>
  <summary> (expand) admin.py Pep8 found 0 errors:</summary>

![admin.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_products_admin.png)

</details>

<details>
  <summary> (expand) apps.py Pep8 found 0 errors:</summary>

![apps.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_products_apps.png)

</details>

<details>
  <summary> (expand) forms.py Pep8 found 0 errors:</summary>

![forms.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_products_forms.png)

</details>

<details>
  <summary> (expand) models.py Pep8 found 0 errors:</summary>

![models.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_products_models.png)

</details>

<details>
  <summary> (expand) test_forms.py Pep8 found 0 errors:</summary>

![test_forms.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_products_test_forms.png)

</details>

<details>
  <summary> (expand) test_models.py Pep8 found 0 errors:</summary>

![test_models.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_products_test_models.png)

</details>

<details>
  <summary> (expand) test_views.py Pep8 found 0 errors:</summary>

![test_views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_products_test_views.png)

</details>

<details>
  <summary> (expand) urls.py Pep8 found 0 errors:</summary>

![urls.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_products_urls.png)

</details>

<details>
  <summary> (expand) views.py Pep8 found 0 errors:</summary>

![views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_products_views.png)

</details>

<details>
  <summary> (expand) widgets.py Pep8 found 0 errors:</summary>

![widgets.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_products_widgets.png)

</details>

[Back to Top](#testing-documentation)


### Profiles App:

<details>
  <summary> (expand) apps.py Pep8 found 0 errors:</summary>

![apps.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_profiles_apps.png)

</details>

<details>
  <summary> (expand) forms.py Pep8 found 0 errors:</summary>

![forms.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_profiles_forms.png)

</details>

<details>
  <summary> (expand) models.py Pep8 found 0 errors:</summary>

![models.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_profiles_models.png)

</details>

<details>
  <summary> (expand) test_forms.py Pep8 found 0 errors:</summary>

![test_forms.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_profiles_test_forms.png)

</details>

<details>
  <summary> (expand) test_models.py Pep8 found 0 errors:</summary>

![test_models.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_profiles_test_models.png)

</details>

<details>
  <summary> (expand) test_views.py Pep8 found 0 errors:</summary>

![test_views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_profiles_test_views.png)

</details>

<details>
  <summary> (expand) urls.py Pep8 found 0 errors:</summary>

![urls.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_profiles_urls.png)

</details>

<details>
  <summary> (expand) views.py Pep8 found 0 errors:</summary>

![views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_profiles_views.png)

</details>


### Wishlist App:

<details>
  <summary> (expand) admin.py Pep8 found 0 errors:</summary>

![admin.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_wishlist_admin.png)

</details>

<details>
  <summary> (expand) apps.py Pep8 found 0 errors:</summary>

![apps.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_wishlist_apps.png)

</details>

<details>
  <summary> (expand) models.py Pep8 found 0 errors:</summary>

![models.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_wishlist_models.png)

</details>

<details>
  <summary> (expand) test_views.py Pep8 found 0 errors:</summary>

![test_views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_wishlist_test_views.png)

</details>

<details>
  <summary> (expand) urls.py Pep8 found 0 errors:</summary>

![urls.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_wishlist_urls.png)

</details>

<details>
  <summary> (expand) views.py Pep8 found 0 errors:</summary>

![views.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_wishlist_views.png)

</details>


### Root modules:

<details>
  <summary> (expand) manage.py Pep8 found 0 errors:</summary>

![manage.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_manage.png)

</details>

<details>
  <summary> (expand) custom_storages.py Pep8 found 0 errors:</summary>

![custom_storages.py Pep8 Tests](/docs/test_img/pep8_validator/pep8_valid_custom_storages.png)

</details>

# Physical Testing

## Devices used for physical testing: 

* Samsung Galaxy S8,
* Samsung Tab A 9.7-inch tablet,
* 17-inch 1080p Laptop (Google Chrome, Mozilla Firefox, Opera, Microsoft Edge browsers),
* 24-inch 1080p Display (Google Chrome, Mozilla Firefox, Opera, Microsoft Edge browsers),
* 32-inch 2040p Display (Google Chrome, Mozilla Firefox, Opera, Microsoft Edge browsers).

Application performs as intended on all devices.


[Back to Top](#testing-documentation)


# Testing of User Stories

_GitHub does not allow videos hosted in the local repository to be played on the repository page.
Although when viewing on GitHub these videos appear fine, they might not be available in this format if this project is forked. Please refer to the Local Links if needed._

## New User Stories

### 1. As a new user, I want to be able to create and register an account.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Registration Page | On landing page, expand the "Account" dropdown menu and click "Register". Fill in the form with your information and submit the form. | To receive a confirmation link in the email address I registered with. | Works as expected. |

<details>
  <summary> (Expand - User Story 1 testing video) </summary>


https://user-images.githubusercontent.com/79543676/165307613-ffcf3070-a4ac-4df9-a6d4-96e17838b638.mp4

  [Local Link](/docs/test_user_stories/user_story_1.mp4)

</details>


### 2. As a new user, I want to be able to login and access my account.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Login Page | Expand the "Account" dropdown menu and click "Login". Fill in the form with your login information and submit the form. | Gain access to previously registered account. | Works as expected. |

<details>
  <summary> (Expand - User Story 2 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165307816-ea68407b-76ca-4952-8e4d-d7f32634a756.mp4

  [Local Link](/docs/test_user_stories/user_story_2.mp4)

</details>


### 3. As a new user, I want to be able to logout.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Logout Page | Expand the "Account dropdown menu and click "Logout". On the Logout Page confirm your action. | To no longer be logged in on the site. | Works as expected. |

<details>
  <summary> (Expand - User Story 3 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165307918-c7b3be3f-7b40-46d5-b8cb-8d350fd49559.mp4

  [Local Link](/docs/test_user_stories/user_story_3.mp4)

</details>

[Back to Top](#testing-documentation)


### 4. As a new user, I want to browse the store's merchandise.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Products Page | Select "All Products" button in the main navigation. | To view all products in the store. | Works as expected. |

<details>
  <summary> (Expand - User Story 4 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165308094-65d95f38-5252-4908-bc12-6deb830b1da5.mp4

  [Local Link](/docs/test_user_stories/user_story_4.mp4)

</details>


### 5. As a new user, I want to be able to search for specific products.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Search bar on top header navigation | From any page, click the search bar and input search parameters. | To see a selection of products that contain the search parameters in the name or description. | Works as expected. |

<details>
  <summary> (Expand - User Story 5 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165308133-615c174c-6f88-4217-b7e9-a223e7f36bde.mp4

  [Local Link](/docs/test_user_stories/user_story_5.mp4)

</details>


### 6. As a new user, I want to be able to browse by categories.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Main navigation menu | From any page, expand the category dropdowns and select a subcategory. | To see the products belonging to the selected category. | Works as expected. |

<details>
  <summary> (Expand - User Story 6 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165309378-e9e6079b-44bc-487e-9bfb-7326ca10a0f2.mp4

  [Local Link](/docs/test_user_stories/user_story_6.mp4)

</details>


### 7. As a new user, I want to be able to sort product lists by price, rating, category or name.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| "All products dropdown in main navigation and "sort by" element on products page | Expand the dropdown/select element and choose the sort criteria. | For the products to be sorted by the chosen criteria. | Works as expected. |

<details>
  <summary> (Expand - User Story 7 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165308399-4353d913-55cf-4bd2-ae32-fc799e2451e9.mp4

  [Local Link](/docs/test_user_stories/user_story_7.mp4)

</details>


### 8. As a new user, I want to view individual product details.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Product details page | Click on a product card. | To view the selected product's details page. | Works as expected. |

<details>
  <summary> (Expand - User Story 8 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165308431-5e18942d-b540-42c4-b13b-d2894d9aa0f6.mp4

  [Local Link](/docs/test_user_stories/user_story_8.mp4)

</details>

[Back to Top](#testing-documentation)


### 9. As a new user, I want to select the different quantities and sizes for a product.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Product details page | Input different quantity in the "Quantity" input and choose a different size from from the "Size" selector before adding the product to the cart. | For the selected quantity and size to be added to the cart. | Works as expected. |

<details>
  <summary> (Expand - User Story 9 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165308490-ca249bd8-b069-41fe-8481-8175bb128be8.mp4

  [Local Link](/docs/test_user_stories/user_story_9.mp4)

</details>


### 10. As a new user, I want to be able to add products to my shopping cart.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Product details page | Click add to cart button. | For the product to be added to my shopping cart. | Works as expected. |

<details>
  <summary> (Expand - User Story 10 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165309451-a59c8def-3308-425c-8849-90762719d723.mp4

  [Local Link](/docs/test_user_stories/user_story_10.mp4)

</details>


### 11. As a new user, I want to be able to add products to a list of interests(wishlist).

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Product details page | Click the "Add to wishlist" link. | For the product to be added to my wishlist and the "Add to wishlist" link to change to "Remove from wishlist" link. | Works as expected. |

<details>
  <summary> (Expand - User Story 11 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165309516-e6fa0663-1aa7-4f21-b073-118af724cf7a.mp4

  [Local Link](/docs/test_user_stories/user_story_11.mp4)

</details>


### 12. As a new user, I want to be able to view the total cost of my shopping cart while I browse.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Shopping cart link in top header navigation and cart preview in toast success messages | Add products to the shopping cart. | For the total cost update in to header navigation and cart preview toast message. | Works as expected. |

<details>
  <summary> (Expand - User Story 12 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165309548-c3fe85f5-8f6c-4508-8531-282c9f8dea6a.mp4

  [Local Link](/docs/test_user_stories/user_story_12.mp4)

</details>

[Back to Top](#testing-documentation)


### 13. As a new user, I want to access and view my shopping cart.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Shopping cart page and cart preview in toast messages | Click the shopping cart link in to header navigation. | To view my shopping cart. | Works as expected. |

<details>
  <summary> (Expand - User Story 13 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165309589-4d78bcf8-88d1-4f74-b3c6-fd960b92fce1.mp4

  [Local Link](/docs/test_user_stories/user_story_13.mp4)

</details>


### 14. As a new user, I want to adjust and manage the products in my shopping cart.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Shopping cart page | For each product select different quantity and click "Update" or remove the product by clicking "Remove" button. | For the shopping cart to be updated with my new preferences. | Works as expected. |

<details>
  <summary> (Expand - User Story 14 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165309623-00e33c43-342e-4b38-8a04-80dd23f2bdfe.mp4

  [Local Link](/docs/test_user_stories/user_story_14.mp4)

</details>


### 15. As a new user, I want to be able to purchase the selected products by entering my payment information in a secure way.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Checkout page | From shopping cart page click "Secure Checkout" and enter payment information in the Stripe "Payment" element. | For my payment information to be handled directly by the payment provider. | Works as expected. |

<details>
  <summary> (Expand - User Story 15 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165309657-58cff9be-1e5c-4b8a-8b21-bf9d716663f4.mp4

  [Local Link](/docs/test_user_stories/user_story_15.mp4)

</details>


### 16. As a new user, I want to view an order confirmation.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Checkout success page | Fill in the delivery details and payment information then click "Complete Order". | For an order confirmation to be displayed. | Works as expected. |

<details>
  <summary> (Expand - User Story 16 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165309692-ddb905bf-9f59-422b-bfd1-5df84fa47ea0.mp4

  [Local Link](/docs/test_user_stories/user_story_16.mp4)

</details>

[Back to Top](#testing-documentation)


### 17. As a new user, I want to receive the order confirmation via e-mail also.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Checkout success page | Fill in the delivery details and payment information then click "Complete Order". | Check your email for the order confirmation. | Works as expected. |

<details>
  <summary> (Expand - User Story 17 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165309727-caae5c59-9200-4f0c-972d-86d36022021d.mp4

  [Local Link](/docs/test_user_stories/user_story_17.mp4)

</details>


## Returning User Stories

### 18. As a returning user, I want to store my delivery information for easy future checkouts.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Profile Page | While logged in, expand the "Account" dropdown menu from top header navigation and click the "Profile" link. Fill in the form with your delivery details | To view the checkout page form already filled with my delivery information. | Works as expected. |

<details>
  <summary> (Expand - User Story 18 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165310426-fd347e30-f8f8-4ab0-9fb1-be4a156e7b81.mp4

  [Local Link](/docs/test_user_stories/user_story_18.mp4)

</details>


### 19. As a returning user, I want to view a record of my past orders.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Profile Page | While logged in, expand the "Account" dropdown menu from top header navigation and click the "Profile" link. | To see my order history. | Works as expected. |

<details>
  <summary> (Expand - User Story 19 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165310464-52042d38-a966-49fa-81ce-8961e0ed05de.mp4

  [Local Link](/docs/test_user_stories/user_story_19.mp4)

</details>


### 20. As a returning user, I want to view and manage my wishlist.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Wishlist Page | While logged in, expand the "Account" dropdown menu from top header navigation and click the "Wishlist" link. | To view a collection of the products I added to my wishlist. | Works as expected. |

<details>
  <summary> (Expand - User Story 20 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165310507-47a59f2b-a5f3-488d-8d18-c02f36d8dfa6.mp4

  [Local Link](/docs/test_user_stories/user_story_20.mp4)

</details>

[Back to Top](#testing-documentation)


### 21. As a returning user, I want to review, rate and read other user's reviews for the products on the site.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Product Details Page | Click the "Leave a review" link. Select a rating and add a review for the product. | For the product's rating to update and my review to show up in the "Reviews" section. | Works as expected. |

<details>
  <summary> (Expand - User Story 21 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165310547-7809e2ae-5540-4495-92d4-daf51f7cd049.mp4

  [Local Link](/docs/test_user_stories/user_story_21.mp4)

</details>


### 22. As a returning user, I want the ability to recover my password.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Login Page | While logged out, access the login page and click "forgot password". Enter your email address and click "Reset my Password" | To receive a reset link in my email. | Works as expected. |

<details>
  <summary> (Expand - User Story 22 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165310577-8a022511-c278-4531-87aa-4ba3ec5304a6.mp4

  [Local Link](/docs/test_user_stories/user_story_22.mp4)

</details>


### 23. As a returning user, I want to view articles related to the store products and the community it caters to.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Th Blog Page | On the main navigation click the "Blog" link. | To view the articles posted on the site. | Works as expected. |

<details>
  <summary> (Expand - User Story 23 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165310640-c9b74862-1b06-4117-acbd-0b880cf733c1.mp4

  [Local Link](/docs/test_user_stories/user_story_23.mp4)

</details>


### 24. As a returning user I want to be able to post, edit or remove articles from the blog section.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| The Blog Page | On the blog page click "Post Article" over the articles accordion. Fill in the form and submit. | To view the article in the accordion with options to "Remove" and "Edit". | Works as expected. |

<details>
  <summary> (Expand - User Story 24 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165310674-0a491a09-040c-4cd3-ad09-9506f17c2204.mp4

  [Local Link](/docs/test_user_stories/user_story_24.mp4)

</details>


### 25. As a returning user, I want to be able to comment on articles.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Blog Post Page | While logged in, click "Read More" on any of the articles. Click "Post a comment", fill in the form and submit. | To view my comment in the post's comment section. | Works as expected. |

<details>
  <summary> (Expand - User Story 25 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165310702-641ed673-d90a-47aa-af87-8353214214bc.mp4

  [Local Link](/docs/test_user_stories/user_story_25.mp4)

</details>

[Back to Top](#testing-documentation)


## Super Users Stories

### 26. As a super user, I want to add content to the store.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Floating Action Button (FAB) | While logged in as superuser, click the Floating Action button on the bottom right hand of the screen to expand. Click the "Add product" link with a "+" icon. Fill in the "add product" form and submit. | To see the product added to the store. | Works as expected. |

<details>
  <summary> (Expand - User Story 26 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165311651-2ce9e4c2-7f68-40e7-853f-559198054a1c.mp4

  [Local Link](/docs/test_user_stories/user_story_26.mp4)

</details>


### 27. As a super user, I want to edit existing content.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Edit buttons on product cards, product detail page and blog accordion | While logged in as a superuser click the "Edit" button with a "pencil" icon on a product or blog article. Update the form and submit. | To view my updates on the product or article. | Works as expected. |

<details>
  <summary> (Expand - User Story 27 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165311692-cac0a886-02c2-4271-8d4f-087b460f28de.mp4

  [Local Link](/docs/test_user_stories/user_story_27.mp4)

</details>


### 28. As a super user, I want to delete existing content.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Delete buttons on product cards, product detail page and blog accordion | While logged in as a superuser click the "Delete" button with a "bin" icon on a product or blog article. Confirm removal in the pop-up modal. | For the product or article to be removed from the site. | Works as expected. |

<details>
  <summary> (Expand - User Story 28 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165311711-ed770c23-3219-4b44-928b-744ae39bd578.mp4

  [Local Link](/docs/test_user_stories/user_story_28.mp4)

</details>


### 29. As a super user, I want to access the administration portal.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Floating Action Button (FAB) | While logged in as superuser, click the Floating Action button on the bottom right hand of the screen to expand. Click the "Admin Dashboard" link with a wrench and screwdriver icon. | To view the Django admin dashboard. | Works as expected. |

<details>
  <summary> (Expand - User Story 29 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165311755-671bb294-e2ef-4920-9444-a6110d522727.mp4

  [Local Link](/docs/test_user_stories/user_story_29.mp4)

</details>

[Back to Top](#testing-documentation)


## Site Owner Stories

### 30. As a site owner, I want the site to be responsive.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Landing Page and Navbar | Change the width of the browser. | For the site to adapt to the new sizes and main navbar to collapse. | Works as expected. |

<details>
  <summary> (Expand - User Story 30 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165312058-e84584a6-53d8-433b-b016-9fdda3b1c90f.mp4

  [Local Link](/docs/test_user_stories/user_story_30.mp4)

</details>


### 31. As a site owner, I want to showcase my social media.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Footer | Scroll down to the footer. Click on the social media links. | For the links to open in new tabs. | Works as expected. |

<details>
  <summary> (Expand - User Story 31 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165312089-431cedd4-68d5-4e23-a0cd-32c0b8d21360.mp4

  [Local Link](/docs/test_user_stories/user_story_31.mp4)

</details>


### 32. As a site owner, I want to provide feedback to the user based on their interactions with the site.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Toast messages system and error pages. | Interact with the features on the site or try to access broken links. | To view the errors/confirmations as toast message or as custom error page. | Works as expected. |

<details>
  <summary> (Expand - User Story 32 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165312124-471b2630-3044-458f-a625-bb4c85e692c4.mp4

  [Local Link](/docs/test_user_stories/user_story_32.mp4)

</details>


### 33. As a site owner, I want forms to be validated on the front-end for better user experience.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Front-end validation on forms | Input erroneous information in a form. | View the validation feedback and being blocked from submitting form until errors are corrected. | Works as expected. |

<details>
  <summary> (Expand - User Story 33 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165312171-0467ec3f-4f97-4b7c-8be9-a9b59ecaec32.mp4

  [Local Link](/docs/test_user_stories/user_story_33.mp4)

</details>


### 34. As a site owner, I want forms to be validated on the back-end in case front-end is bypassed or fails.

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Back-end validation on forms | Submit login form with erroneous information. | Being prevented from logging in and seeing an error message. | Works as expected. |

<details>
  <summary> (Expand - User Story 34 testing video) </summary>

https://user-images.githubusercontent.com/79543676/165312198-4006769f-3466-47f5-a05a-18865f194691.mp4

  [Local Link](/docs/test_user_stories/user_story_34.mp4)

</details>


[Back to Top](#testing-documentation)

# Bugs

## Bug 1: 

**Console error when clicking remove item from shopping cart:**

```
POST http://127.0.0.1:8000/cart/remove/56/ 403 (Forbidden) 		jquery-3.6.0.min.js:2 
```

**Terminal was showing:**

```
Forbidden (CSRF token missing or incorrect.): /cart/remove/56/
[16/Mar/2022 20:39:50] ←[31;1m"POST /cart/remove/56/ HTTP/1.1" 403 2519←[0m         
```
### Fix:

**Get the form CSRF token generated by Django through a data attribute on the button:**

Add: ```data-token="{{ csrf_token }}"``` to the button

Add: ```var csrfToken = $(this).data('token');``` to the script


## Bug 2:

**When using Bootstrap 5.1 toast boilerplate:**

```html
<div role="alert" aria-live="assertive" aria-atomic="true" class="toast" data-bs-autohide="false">
  <div class="toast-header">
    <img src="..." class="rounded me-2" alt="...">
    <strong class="me-auto">Bootstrap</strong>
    <small>11 mins ago</small>
    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
  </div>
  <div class="toast-body">
    Hello, world! This is a toast message.
  </div>
</div>
```

**Would trigger:**

```
Triggers:
Internal Server Error: /products/...
Traceback (most recent call last):
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\fields\__init__.py", line 1823, in get_prep_value  
    return int(value)
ValueError: invalid literal for int() with base 10: '...'

```

**Which was a result of:**

```
Traceback (most recent call last):
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\core\handlers\exception.py", line 47, in inner
    response = get_response(request)
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\products\views.py", line 73, in product_detail
    product = get_object_or_404(Product, pk=product_id)
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\shortcuts.py", line 76, in get_object_or_404
    return queryset.get(*args, **kwargs)
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\query.py", line 424, in get
    clone = self._chain() if self.query.combinator else self.filter(*args, **kwargs)
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\query.py", line 941, in filter
    return self._filter_or_exclude(False, args, kwargs)
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\query.py", line 961, in _filter_or_exclude
    clone._filter_or_exclude_inplace(negate, args, kwargs)
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\query.py", line 968, in _filter_or_exclude_inplace 
    self._query.add_q(Q(*args, **kwargs))
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\sql\query.py", line 1396, in add_q
    clause, _ = self._add_q(q_object, self.used_aliases)
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\sql\query.py", line 1415, in _add_q
    child_clause, needed_inner = self.build_filter(
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\sql\query.py", line 1350, in build_filter
    condition = self.build_lookup(lookups, col, value)
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\sql\query.py", line 1196, in build_lookup
    lookup = lookup_class(lhs, rhs)
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\lookups.py", line 25, in __init__
    self.rhs = self.get_prep_lookup()
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\lookups.py", line 77, in get_prep_lookup
    return self.lhs.output_field.get_prep_value(self.rhs)
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\fields\__init__.py", line 1825, in get_prep_value  
    raise e.__class__(
ValueError: Field 'id' expected a number but got '...'.
[17/Mar/2022 01:20:31] ←[35;1m"GET /products/... HTTP/1.1" 500 142907←[0m
```


### Fix:

**Remove the image field from the toast:**

```html 
<img src="..." class="rounded me-2" alt="...">
```

[Back to Top](#testing-documentation)


## Bug 3:

**When trying to adjust quantity of item in cart with no size even though items with sizes worked as intended**

```
TypeError at /cart/adjust/85/
'dict' object is not callable
Request Method:	POST
Request URL:	http://127.0.0.1:8000/cart/adjust/85/
Django Version:	3.2
Exception Type:	TypeError
Exception Value:	'dict' object is not callable
```

### Fix:

**Wrong brackets were used in attached operation message: ```cart(item_id)``` supposed to be ```cart[item_id]```**


## Bug 4:

**When trying to dump local database with command suggested in the course:**

```
$ py manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
```

**Would result in:**

```
CommandError: Unable to serialize database: 'charmap' codec can't encode character '\u2008' in position 462: character maps to <undefined>
Exception ignored in: <generator object cursor_iter at 0x00000135E28A2200>
Traceback (most recent call last):
  File "C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\db\models\sql\compiler.py", line 1625, in cursor_iter        
    cursor.close()
sqlite3.ProgrammingError: Cannot operate on a closed database.
```

### Solution:

```
py -Xutf8 manage.py dumpdata --exclude auth.permission --exclude contenttypes > data.json
```

Credit for solution to [StackOverflow](https://stackoverflow.com/a/67336562)

[Back to Top](#testing-documentation)


## Bug 5:

**Posting a review with an empty string would result in:**

```
NoReverseMatch at /reviews/post/
Reverse for 'product_detail' with arguments '('',)' not found. 1 pattern(s) tried: ['products/(?P<product_id>[0-9]+)/$']
Request Method:	POST
Request URL:	http://127.0.0.1:8000/reviews/post/
Django Version:	3.2
Exception Type:	NoReverseMatch
Exception Value:	Reverse for 'product_detail' with arguments '('',)' not found. 1 pattern(s) tried: ['products/(?P<product_id>[0-9]+)/$']
Exception Location:	C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\lib\site-packages\django\urls\resolvers.py, line 694, in _reverse_with_prefix
Python Executable:	C:\Users\Mortis Vivis\Documents\GitHub\MS4_MotoStyle\virtualenv\Scripts\python.exe
Python Version:	3.9.6
```

### Fix:

**Added front-end form validation that prevents submission with empty strings and displays warning to the user:**

```
// Calls the validate method on the review form
$('#reviewModal').find('form').validate({
    // Validation Rules
    rules: {
        comment: {
            notEmptyString: true,
        }
    },
    messages: {
        comment: {
            notEmptyString: 'No empty strings please.',
        },
    },
})
```


## Bug 6:

Floating action button with sticky position would trigger extra clicks on mobile and tablets when at the bottom of the page due to footer displacement.

### Fix: 

Changed position to fixed and added extra media queries so it wouldn’t overlap with footer:

```css
@media screen and (max-width: 992px) {

    .floating-container {
        position: fixed;
        width: 100px;
        height: 100px;
        bottom: 20%;
        right: 0;
    }
}

@media screen and (max-width: 768px) {
    .floating-container {
        position: fixed;
        width: 100px;
        height: 100px;
        bottom: 30%;
        right: 0;
    }
}
```


## Bug 7:

Stripe webhook would return status 500 and order confirmation email would not be sent:

![Stripe CLI](/docs/test_img/bugs/stripe_cli_500.jpg)

### Fix:

I added extra fields in my profile model for full_name and email which were causing sync issues when the webhook was checking the orders associated with the profile in the database thus sending status 500 back to Stripe.
After removing those extra fields the webhook response status is 200 and email order confirmations are being sent successfully:

![Webhook fixed](/docs/test_img/bugs/webhook_fixed.png)

[Back to Top](#testing-documentation)


