# Imports
# 3rd party:
from django.contrib import admin
from django.urls import path
# Internal
from . import views
# -----------------------------------------------------------------------------


urlpatterns = [
    path('', views.index, name='home')
]
