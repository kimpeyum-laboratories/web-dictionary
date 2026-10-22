from django.urls import path
from .views import EntryView, search

urlpatterns = [
    path("entry/<str:name>", EntryView.as_view(), name="entry"),
    path("search", search, name="search"),
]
