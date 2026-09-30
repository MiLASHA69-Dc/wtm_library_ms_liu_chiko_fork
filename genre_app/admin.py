from django.contrib import admin
from .models import Genre
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    list_display = [
        "id","title","category"
    ]
