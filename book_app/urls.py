from django.urls import path
from .views import display_books

app_name="books_app"
urlpatterns =[
    path("display-books/",display_books,name="display_books")
]