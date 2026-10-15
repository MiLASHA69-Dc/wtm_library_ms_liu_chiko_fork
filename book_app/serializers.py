from .models import Book,BookRequest
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
            model = Book
            fields = [
                "title",
                "isbn",
                "author",
                "genre",
                "published_date",
            ]