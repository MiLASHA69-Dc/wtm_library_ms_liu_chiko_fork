from django.contrib import admin
from .models import Author
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = [
#         "id",'first_name','last_name','dob','year_of_death'
#     ]
class AuthorAdmin(ImportExportModelAdmin):
    list_display = [
        "id",'first_name','last_name','dob','year_of_death'
    ]

admin.site.register(Author,AuthorAdmin)
