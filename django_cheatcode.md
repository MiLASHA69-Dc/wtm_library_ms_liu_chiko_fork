# Django Quick Reference & Cheat Code

A practical cheat sheet built for the Women Techmakers Mentorship Program covering setup, CLI ORM queries, CRUD workflows, templates, and database commands.

---

## 1. Environment & Setup

### **Virtual Environment & Dependencies (`uv`)**
```bash
# Create virtual environment
uv venv .venv

# Activate environment (PowerShell)
.venv\Scripts\Activate.ps1

# Install Django and dependencies
uv pip install django psycopg2-binary
```

### **Project & App Initialization**
```bash
# Start a new Django project
django-admin startproject myproject .

# Create a new Django app
python manage.py startapp myapp
```

---

## 2. Configuration (`project/settings.py`)

### **Register Applications & Configure Database**
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Custom Apps
    "myapp",
]

# Database Setup (Default SQLite or PostgreSQL)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

---

## 3. Database & Models (`myapp/models.py`)

### **Defining Model Schemas**
```python
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author.name}"
```

### **Migrations & Management Commands**
```bash
# Generate migration files from model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create superuser for Django Admin
python manage.py createsuperuser

# Start interactive Python shell with Django loaded
python manage.py shell

# Start development server
python manage.py runserver
```

---

## 4. Interactive Django Shell / CLI ORM Commands

Launch the shell using `python manage.py shell`:

```python
from myapp.models import Author, Book

# --- CREATE ---
# Method 1: Save instance
author1 = Author(name="Jane Doe", email="jane@example.com")
author1.save()

# Method 2: Direct creation
author2 = Author.objects.create(name="John Smith", email="john@example.com")

# --- READ / QUERY ---
# Fetch all records
all_authors = Author.objects.all()

# Filter matching records (returns QuerySet)
active_books = Book.objects.filter(is_available=True)
jane_books = Book.objects.filter(author__name="Jane Doe")

# Order records
sorted_authors = Author.objects.all().order_by("name")  # Ascending
recent_authors = Author.objects.all().order_by("-created_at")  # Descending

# Fetch a single object (raises exception if not found or if multiple returned)
single_author = Author.objects.get(id=1)
specific_email = Author.objects.get(email="jane@example.com")

# First or Last item safely
first_author = Author.objects.first()

# --- UPDATE ---
single_author.name = "Jane H. Doe"
single_author.save()

# Bulk update
Book.objects.filter(is_available=False).update(is_available=True)

# --- DELETE ---
single_author.delete()
```

---

## 5. URL Routing & Dispatching

### **Project Router (`project/urls.py`)**
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("authors/", include("myapp.urls", namespace="myapp")),
]
```

### **App Router (`myapp/urls.py`)**
```python
from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("", views.author_list, name="author_list"),
    path("<int:pk>/", views.author_detail, name="author_detail"),
    path("create/", views.author_create, name="author_create"),
    path("<int:pk>/delete/", views.author_delete, name="author_delete"),
]
```

---

## 6. Views & Query Logic (`myapp/views.py`)

### **CRUD Views with ORM Querying**
```python
from django.shortcuts import get_object_or_404, redirect, render
from .models import Author


# 1. Fetch & Show All Items (Filtered and Ordered)
def author_list(request):
    # Fetch all, filter active ones, and order by name
    authors = Author.objects.all().order_by("name")

    # Dynamic filter via request parameters (e.g. ?search=jane)
    search_query = request.GET.get("search")
    if search_query:
        authors = authors.filter(name__icontains=search_query)

    return render(request, "myapp/author_list.html", {"authors": authors})


# 2. Get Single Item by Primary Key
def author_detail(request, pk):
    # Safe retrieval using get() under the hood; returns 404 if not found
    author = get_object_or_404(Author, pk=pk)
    return render(request, "myapp/author_detail.html", {"author": author})


# 3. Create Item
def author_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        bio = request.POST.get("bio", "")

        Author.objects.create(name=name, email=email, bio=bio)
        return redirect("myapp:author_list")

    return render(request, "myapp/author_form.html")


# 4. Delete Item
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        author.delete()
        return redirect("myapp:author_list")

    return render(
        request, "myapp/author_confirm_delete.html", {"author": author}
    )
```

---

## 7. Django Admin (`myapp/admin.py`)

```python
from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "created_at"]
    search_fields = ["name", "email"]
    ordering = ["name"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "is_available"]
    list_filter = ["is_available"]
    search_fields = ["title", "author__name"]
```

---

## 8. Templates & Dynamic Tags (`templates/myapp/author_list.html`)

```html
{% extends "base.html" %}

{% block content %}
<h2>Author Directory</h2>

<!-- Search Filter Form -->
<form method="GET" action="{% url 'myapp:author_list' %}">
    <input type="text" name="search" placeholder="Search authors..." value="{{ request.GET.search }}">
    <button type="submit">Search</button>
</form>

<ul>
    {% for author in authors %}
        <li>
            <a href="{% url 'myapp:author_detail' author.pk %}">
                <strong>{{ author.name }}</strong>
            </a> 
            - {{ author.email }}
            
            <form action="{% url 'myapp:author_delete' author.pk %}" method="POST" style="display:inline;">
                {% csrf_token %}
                <button type="submit">Delete</button>
            </form>
        </li>
    {% empty %}
        <li>No authors found matching your criteria.</li>
    {% endfor %}
</ul>
{% endblock %}
```
