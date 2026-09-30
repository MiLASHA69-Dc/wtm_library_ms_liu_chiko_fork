from django.db import models
from author.models import Author
from genre_app.models import Genre
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200,blank=False,null=False)
    isbn = models.CharField(max_length=40,blank=False,null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    published_date = models.DateField(null=False,blank=False)

    # for admin log audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}-{self.isbn}"