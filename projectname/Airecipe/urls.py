from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_recipe, name='generate_recipe'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/', views.add_to_wishlist, name='add_to_wishlist'),
]
