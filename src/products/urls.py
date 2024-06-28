from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    path("products/", view=views.ProductIndexView.as_view(), name="index"),
    path("products/<int:pk>/", view=views.ProductDetailView.as_view(), name="detail"),
    path("cart/", view=views.cart, name="cart"),
]
