from django.urls import path
from . import views

urlpatterns = [
    path('',views.home2, name='index-page'),
    path('generate/',views.generate,name="generate-page"),
    path('wishlist/',views.wishlist,name="wishlist-page"),
]