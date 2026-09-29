# WTM Library Management System (`library_ms`)

A modular Django-based Library Management System developed as part of the **Women Techmakers (WTM) Bambili × Gwarinpa Mentorship Program 2026**.

This project demonstrates core backend web development concepts, including environment isolation, dependency management with `uv`, modular Django app architecture, custom URL routing, and Git version control.

---

## 🛠️ Tech Stack & Environment

- **Language:** Python 3.12+
- **Framework:** Django 5.x
- **Environment & Dependency Manager:** [`uv`](https://github.com/astral-sh/uv)
- **Version Control:** Git & GitHub

---


---

## 🚀 Initial Development Setup & Workflow

If you are setting up the project from scratch, the following workflow was executed:

### 1. Initialize Git & `uv` Project
```bash
# Initialize git and uv project
git init
uv init

# Install Django package
uv add django

# Lock dependencies to requirement_dev.txt
uv pip freeze > requirement_dev.txt
```

### 2. Initialize Django Project
Create the root Django project in the current working directory:
```bash
django-admin startproject library_ms .
```
> **Note:** Adding `.` at the end prevents redundant nested directories (e.g., `library_ms/library_ms/`).

Run the initial development server to verify setup:
```bash
python manage.py runserver
```

---

## 🏗️ Creating and Configuring the `author` App

### 1. Generate Application
```bash
python manage.py startapp author
```

### 2. Register Application in Settings
Register the app in `library_ms/settings.py`:
```python
INSTALLED_APPS = [
    # Built-in Django apps...
    "author",
]
```

---

## 🔗 Routing & Views Setup

### 1. App-Level View (`author/views.py`)
Defined an initial HTTP view function to verify route handling:
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def author_view(request):
    return HttpResponse(
        "<h2>This is a registered Author Application</h2> "
        "<strong>Yeay our first application in Django under development </strong>"
    )
```

### 2. App-Level URL Configuration (`author/urls.py`)
Created `author/urls.py` to keep routing modular and decoupled from the main project settings:
```python
from django.urls import path
from .views import author_view

urlpatterns = [
    path("display/", author_view),
]
```

### 3. Root URL Integration (`library_ms/urls.py`)
Included `author.urls` into the primary project router:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("author/", include("author.urls")),
]
```
> **Route Access:** `http://127.0.0.1:8000/author/display/`

---

## 📦 Version Control & GitHub Remote Setup

Track files, perform the initial commit, rename the default branch to `main`, and push to GitHub:
```bash
# Stage all project files
git add .

# Create initial commit
git commit -m "feat: initial project setup with uv, django, and author app routing"

# Set primary branch to main
git branch -M main

# Add remote repository link
git remote add origin https://github.com/YOUR_USERNAME/wtm_library.git

# Push changes and set upstream tracking
git push -u origin main
```

### 💡 Fixing Remote URL Misconfigurations
If an incorrect remote repository URL was entered during setup, reset it using:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/wtm_library.git
```
Verify the active remote configuration:
```bash
git remote -v
```

---

## 📂 Directory Structure

```text
wtm_library/
├── .venv/                   # Virtual environment managed by uv
├── author/                  # Author application module
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py             # Custom app-level routing
│   └── views.py            # Author views
├── library_ms/              # Core Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Project settings & INSTALLED_APPS
│   ├── urls.py              # Root URL dispatcher
│   └── wsgi.py
├── .gitignore
├── manage.py
├── pyproject.toml           # uv configuration
├── requirement_dev.txt      # Frozen dependencies
└── README.md
```
----
## 📥 Cloning the Repository & Installation

Follow these steps to clone the repository, set up your virtual environment, and install dependencies using `uv`:

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/wtm_library.git
cd wtm_library
```

----

### 2. Create Virtual Environment with `uv`
```bash
# Create a standard virtual environment (.venv)
uv venv

# Activate virtual environment (Windows PowerShell)
.venv\Scripts\activate

# Activate virtual environment (Linux/macOS)
source .venv/bin/activate
```
-----
### 3. Install Dependencies
Install packages directly using `uv` and the provided requirements file:
```bash
# Install dependencies from requirement_dev.txt
uv pip install -r requirement_dev.txt
```

## ⚙️ Creating More Applications for the library management system

### 1. Modular App Structure
Created app modules to separate concerns across the domain models:
```bash

python manage.py startapp book_app
python manage.py startapp genre_app
```

### 2. Application & Template Registration (`library_ms/settings.py`)
Configured global template directory searching using `os.path.join(BASE_DIR, "templates")` and registered custom apps in `INSTALLED_APPS`:

```python
import os

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Custom Apps
    "author",
    "book_app",
    "genre_app",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

---

## 🗄️ Database Models & Admin Registration

### 1. Author Model (`author/models.py`)
```python
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    dob = models.DateField(null=True, blank=True)
    year_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.dob} {self.year_of_death if self.year_of_death else ''}"
```

### 2. Custom Admin Class (`author/admin.py`)
Customized the Django Admin dashboard display layout for `Author` records:

```python
from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "dob", "year_of_death"]


admin.site.register(Author, AuthorAdmin)
```

### 3. Database Migrations & Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 📝 Forms & Controllers (Views)

### 1. Author ModelForm (`author/forms.py`)
Used Django's `ModelForm` to generate HTML forms mapped directly to the `Author` schema:

```python
from django import forms
from .models import Author


class CreateAuthorEntry(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "first_name",
            "last_name",
            "dob",
            "year_of_death",
        ]
```

### 2. Views Setup (`author/views.py`)
Implemented views for retrieving author lists and processing form submissions using `POST` request handling and URL redirects:

```python
from django.shortcuts import render, redirect
from .models import Author
from .forms import CreateAuthorEntry


def author_view(request):
    all_author = Author.objects.all().order_by("-id")
    return render(
        request,
        "author/display_author.html",
        {"display_all_author": all_author},
    )


def author_entry(request):
    if request.method == "POST":
        author_form = CreateAuthorEntry(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect("display_authors")
    else:
        author_form = CreateAuthorEntry()

    context = {"create_form": author_form}
    return render(request, "author/create_author.html", context)
```

---

## 🔗 URL Routing Configuration

### 1. App-Level Routing (`author/urls.py`)
```python
from django.urls import path
from .views import author_view, author_entry

urlpatterns = [
    path("display/", author_view, name="display_authors"),
    path("create-author/", author_entry, name="create_author"),
]
```

### 2. Root Project Routing (`library_ms/urls.py`)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("author/", include("author.urls")),
]
```

---

## 🎨 Templates & Inheritance Architecture

### 1. Master Base Layout (`templates/base/base.html`)
Provides top-level navigation, document setup, and CSS table styling:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        table, th, td {
            border: 1px solid black;
            border-spacing: 0cap;
        }
    </style>
    <title>{{ title }}</title>
</head>
<body>
    <ul style="list-style: none; display: flex;">
        <li style="margin-right: 50px;"><a href="{% url 'create_author' %}">Create Author</a></li>
        <li><a href="{% url 'display_authors' %}">Display Author List</a></li>
    </ul>
    {% block content %}
      
    {% endblock %}
</body>
</html>
```

### 2. Create Author View (`templates/author/create_author.html`)
Extends `base/base.html` and renders the ModelForm with `{% csrf_token %}` protection:

```html
{% extends "base/base.html" %}

{% block content %}
   <form action="" method="post">
        {% csrf_token %}
        {{ create_form.as_p }}
        <button type="submit">Create</button>
    </form>
{% endblock %}
```

### 3. Display Authors View (`templates/author/display_author.html`)
Renders author listings dynamically with fallback conditional logic (`Still Alive` vs. `year_of_death` date):

```html
{% extends "base/base.html" %}

{% block content %}
   <h2>List of Authors</h2>
    <table>
        <tr>
            <th>S/N</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Date of birth</th>
            <th>Year of Death</th>
            <th colspan="2">Options</th>
        </tr>
        {% for author in display_all_author %}
        <tr>
            <td>{{ forloop.counter }}</td>
            <td>{{ author.first_name }}</td>
            <td>{{ author.last_name }}</td>
            <td>{{ author.dob }}</td>

            {% if author.year_of_death %}
              <td>{{ author.year_of_death }}</td>
            {% else %}
              <td>Still Alive</td>
            {% endif %}
            <td><a href="">edit</a></td>
            <td><a href="">delete</a></td>
        </tr>
        {% endfor %}
    </table>
{% endblock %}
```

---

## 📂 Project Directory Layout

```text
wtm_library/
├── .venv/                      # Virtual environment managed by uv
├── author/                     # Author Domain Module
│   ├── admin.py                # AuthorAdmin configuration
│   ├── forms.py                # CreateAuthorEntry ModelForm
│   ├── models.py               # Author database schema
│   ├── urls.py                 # App routing rules
│   └── views.py                # author_view and author_entry handlers
├── book_app/                   # Books Module
├── genre_app/                  # Genres Module
├── library_ms/                 # Core Project Configuration
│   ├── settings.py             # App registration & template DIRS setup
│   └── urls.py                 # Root URL dispatcher
├── templates/                  # Master Templates Folder
│   ├── base/
│   │   └── base.html           # Layout shell with navigation
│   └── author/
│       ├── create_author.html  # Author creation form template
│       └── display_author.html # Author list table template
├── manage.py
├── pyproject.toml              # uv setup file
└── requirement_dev.txt         # Frozen development dependencies
```
