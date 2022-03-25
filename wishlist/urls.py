# Imports
# 3rd party:
from django.urls import path
# Internal
from . import views
# -----------------------------------------------------------------------------


urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path('add/<product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path(
        'remove/<product_id>/', views.remove_from_wishlist,
        name='remove_from_wishlist'
    ),
]
