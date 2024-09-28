# Blog Application - Django with MySQL

This project is a basic blog application built using Django with a MySQL database. The application includes several core features such as user signup, login, and basic blog functionalities like adding, editing, and managing blog posts. Please note that I am still working on implementing advanced features like admin and user login, as well as authorization for different user roles.

## Setup Instructions

### 1. Install Virtual Environment
To manage dependencies efficiently, set up a virtual environment using the following commands:

```bash
pip install virtualenvwrapper-win
mkvirtualenv name_of_venv
```

Activate the environment:

```bash
workon name_of_venv
```

### 2. Install Django
After activating the virtual environment, install Django:

```bash
pip install django
```

### 3. Create a Django Project
Generate a new Django project by running:

```bash
django-admin startproject name_of_project
```

To run the project:

```bash
cd name_of_project
python manage.py runserver
```

### 4. Django Applications (Apps)
The project is modularized into various apps for better organization:

- **Account**
  - Login
  - Signup
- **Home**
  - Home Page
  - About
  - Contact

To create a new app:

```bash
python manage.py startapp name_of_app
```

### 5. Setting Up MySQL Database

1. Install [XAMPP](https://www.apachefriends.org/index.html) for MySQL.
2. Start Apache & MySQL using the XAMPP Control Panel.
3. Access [phpMyAdmin](http://localhost/phpmyadmin) to create a database named `blog_app`.
4. In your Django project, configure the database connection in `settings.py` under `DATABASES`.

### 6. Install MySQL Client for Django
To integrate Django with MySQL, install the MySQL client library:

```bash
pip install mysqlclient
```

### 7. Migrations

Generate and apply migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Working with Images

For image handling, install the Pillow library:

```bash
pip install Pillow
```

After that, apply the necessary database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Current Tasks

- **Edit Blog**: Implement editing functionality, including image handling.
- **Forms**: Apply Bootstrap to remaining forms for improved UI.
- **Pages**: Add additional pages, URLs, and views as needed.
- **About Page**: Include personal details, an image, and a signature.

---

### Features Under Development

- **Admin & User Login**: A robust admin and user login system with role-based access control.
- **User Authorization**: Implement user permissions and access controls for managing blogs and user accounts.

