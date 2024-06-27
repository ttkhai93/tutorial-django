from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    path("", view=views.IndexView.as_view(), name="index"),
    path("<int:pk>/", view=views.DetailView.as_view(), name="detail"),
]
