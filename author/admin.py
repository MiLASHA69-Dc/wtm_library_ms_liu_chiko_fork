from django.contrib import admin
from .models import Author
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "id",'first_name','last_name','dob','year_of_death'
    ]

admin.site.register(Author,AuthorAdmin)
