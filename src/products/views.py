from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

from .models import Product


class ProductIndexView(generic.ListView):
    template_name = "products/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.all()


class ProductDetailView(generic.DetailView):
    template_name = "products/detail.html"
    model = Product


def cart(request):
    return render(request, "products/cart.html")
