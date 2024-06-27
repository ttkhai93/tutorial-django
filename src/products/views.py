from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

from .models import Product


class IndexView(generic.ListView):
    template_name = "products/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.all()


class DetailView(generic.DetailView):
    template_name = "products/detail.html"
    model = Product
