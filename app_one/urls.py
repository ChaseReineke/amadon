from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index), # Main page, displays shop
    path('purchase', views.purchase), # User clicks buy
    path('checkout', views.checkout), # User is taken to checkout.html from views.purchase
    path('clear', views.clear), # User clears purchase history
]