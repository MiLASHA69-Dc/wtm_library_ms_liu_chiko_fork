from django.db import models
# from author.models import Author
# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=200,blank=False,null=False)
    category = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return f"{self.title}- {self.category}"