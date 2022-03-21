# Imports
# 3rd party:
from django import forms
# Internal
from .models import Product, Category
# -----------------------------------------------------------------------------


class ProductForm(forms.ModelForm):

    