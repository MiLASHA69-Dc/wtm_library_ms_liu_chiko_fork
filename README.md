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
