from django.contrib import admin
from .models import Book
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = [
        "id","title","isbn","author","published_date"
    ]

# admin.site.register(Book,BookAdmin)
