from django.urls import path
from .views import ResourceView, search

urlpatterns = [
    path("entry/<str:name>/", ResourceView.as_view(), name="resource"),
    path("search", search, name="search"),
]
