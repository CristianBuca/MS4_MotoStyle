# Imports
# 3rd party:
from django.urls import path
# Internal
from . import views
# -----------------------------------------------------------------------------


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blog_post_id>/', views.blog_post, name='blog_post'),
    path('add/', views.add_blog_post, name='add_blog_post'),
]
