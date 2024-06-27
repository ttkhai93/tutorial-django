from django.contrib import admin
from django.db import models
from django.forms import TextInput

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "info"]
    search_fields = ["name"]
    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 20})}}


admin.site.register(Product, ProductAdmin)
