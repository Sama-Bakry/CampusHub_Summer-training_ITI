# CampusHub – University Student Portal

CampusHub is a simple university student portal built using Django.

The project demonstrates the main Django concepts covered in the ITI Full Stack Web Development with Python lectures, including:

- Django Project and App
- Models and Database
- Views
- Templates
- URLs
- Django Template Language (DTL)
- DTL Variables, Filters and Tags
- Static Files and CSS
- Django ORM
- Database Migrations
- Django Admin

## Features

- Home page
- Students page
- Student details page
- Courses page
- Course details page
- Departments page
- Django Admin dashboard
- Display data from the database
- CSS styling using static files

## Technologies Used

- Python
- Django
- PostgreSQL
- HTML
- CSS
- Django Template Language (DTL)

## Database Models

The project contains three main models:

- Department
- Course
- Student

## Django Concepts Used

### Models

Django models are used to define the structure of the application's data and create database tables through Django migrations.

### Views

Views handle requests and retrieve data from the database before sending it to templates.

### Templates

HTML templates are used to display the application's pages.

### DTL

The project uses:

- Variables
- Filters
- Tags
- `for` loops
- `url` tag

Example:

```django
{{ student.name|first|upper }}
