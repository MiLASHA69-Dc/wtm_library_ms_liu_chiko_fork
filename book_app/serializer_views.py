from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required

@login_required
@api_view(["GET"])

def book(request):
    all_book =Book.objects.all()
    if request.method=="GET":
        book_serializer = BookSerializer(all_book,many=True)
        return Response(book_serializer.data,status=status.HTTP_200_OK)
    return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)