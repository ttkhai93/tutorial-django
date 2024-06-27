from django.urls import path

from . import views

app_name = "polls"  # Application namespace
urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path("", view=views.IndexView.as_view(), name="index"),
    path("<int:pk>/", view=views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", view=views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", view=views.vote, name="vote"),
]
