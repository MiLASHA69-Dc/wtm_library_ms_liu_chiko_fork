from django.shortcuts import render
from .models import Book
# Create your views here.

def display_books(request):
    all_books = Book.objects.all()
    context = {
        "display_books":all_books
    }
    return render(render,"book/display_books.html",context)
