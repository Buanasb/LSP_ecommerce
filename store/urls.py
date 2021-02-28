from django.urls import path
from .import views


urlpatterns = [
    path('', views.store, name="store"),
    path('description/<int:pk>/', views.description, name="description"),
    path('spec/', views.spec, name="spec"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout")
]
