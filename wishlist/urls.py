# Imports
# 3rd party:
from django.urls import path
# Internal
from . import views
# -----------------------------------------------------------------------------


urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
]
