from django.urls import path
from .views import author_view

urlpatterns = [
    path("display/",author_view)
]
