from atexit import register
from urllib.parse import urlparse
from django.urls import path
from .import views
from clothing.controller import cart, checkout



urlpatterns = [
    path('',views.home, name="home"),
    path('home',views.home, name="home"),
    path('about', views.about, name="about"),
    path('collections', views.collections, name="collections"),
    path('sign-up', views.sign_up, name='sign_up'), 
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),
    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('carts', cart.viewcart, name="carts"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    path('checkout', checkout.index, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder")
    
]