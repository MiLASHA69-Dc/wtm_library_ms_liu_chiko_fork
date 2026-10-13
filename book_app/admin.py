from django.contrib import admin
from .models import Book,BookRequest
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = [
        "id","title","isbn","author","published_date"
    ]

@admin.register(BookRequest)
class BookRequestAdmin(ImportExportModelAdmin):
    list_display = [
        "id","customer","book","book_date_request","book_date_return"
    ]

# admin.site.register(Book,BookAdmin)
