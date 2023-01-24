# Lab Intro to Django

## Project Name - Django Snacks

### Author - Gordon P Reilley Jr

### Feature Tasks and Requirements:

- Create web site in Django with 2 pages
  - home page
  - about page
  - create views/urls/templates as needed for home and about pages
  - use ancestor template to contain navigation elements
  - Should be built the “Django way” aka match the structure of in-class demo

### Implementation Notes

- Typical Steps to Start Django Project
  - create project
  - define app
  - add app to project
  - add views
  - add urlpatterns
  - add templates
  - add tests

### User Acceptance Tests

- Use Django’s built in testing tools
  - Test that `home` and `about` url status codes
  - Test `home` and `about` url template use, including ancestor template.

### Setup

1. Create and activate virtual environment
2. Run `pip install django`
3. Run `django-admin startproject {project name} .`
4. Run `python manage.py runserver` (URL link will show if installation worked) - starts the development server (not used for production). Creates `db.sqlite3` file in `root`.
5. Run `python manage.py migrate` to apply unapplied migrations to the `admin`, `auth`, `contenttypes`, `sessions` apps
6. Run `python manage.py startapp {app name}` to create an app
7. Create a `urls.py` file in your app (not included)
8. Add `snacks` to the `settings.py` file in your project folder in the `INSTALLED APPS` list (with a trailing commma). 
9. Type `from django.views.generic import TemplateView` in the `views.py` file in your app and create the class with context
10. In the ***app*** `urls.py` file create your paths.
11. In the ***project*** `urls.py` file, add `path('', include('snacks.urls')),` to the `urlpatterns` (with a trailing comma) and add `include` to `from django.urls import include, path`.
12. Create `templates` folder in the `root` and create `base.html` and `home.html` and `about.html` files inside.
13. In the `base.html` file, add the normal HTML stuff and inside `<body>`:

    ```
    {% block content %}

    {% endblock content %}
    ```
    
14. In the `home.html` file `{% extends 'base.html' %}` then add context.
15. In the ***project's*** `settings.py` file, in the TEMPLATES section, add `BASE_DIR / 'templates'` to the empty list of `DIRS`.
16. In the ***app's*** `test.py` file, modify and add required tests.
17. Run `python manage.py test` to run the test(s).
18. When creating a new page use ***VUT***:
    * views - add a class to the `views.py` file: 
    
    ```
    class AboutView(TemplateView):
        template_name = 'about.html'
    ```
    
    * urls - add `path('about', AboutView.as_view(), name='about'),` to the `urlpatterns` list. Add `AboutViews` to imports.
    * templates - add `about.html` to the `templates` folder and add the HTML and "pseudo-HTML?"