Install Virtual Envrionment
    pip install virtualenvwrapper-win

Create Virtual Envrionment
    mkvirtualenv name_of_venv

Get in to Virtual Envrionment
    workon name_of_venv

Install Django in Virtual Envrionment
    pip install django

Create Django project
    django-admin startproject name_of_project

To run the project
    Get into name_of_project dir and then run the following command
        python manage.py runserver


Django application are divided into various modules which are said to be as "APPS"
    -   account
            - login
            - signup
    -   home
            - home
            - about
            - contact

Create an "APP"
    -    python manage.py startapp name_of_app


Setting up MYSQL Database
    Install XAMPP
    Start Apache & MYSQL from XAMPP Control Panel
    Goto http://localhost/phpmyadmin in your browser
    Create a new database with the name as "blog_app"

Setup MYSQL database in Django:
    In settings.py, add configuration for above database.

Install MYSQL Client for DJango:
    pip install mysqlclient

Create a migration
    python manage.py makemigrations

Migrate the model
    python manage.py migrate


---------------------------------------------------------------------
To Work with images in python, install the following library first
pip install Pillow

Then, make changes in database
python manage.py makemigrations
python manage.py migrate

Task:
    01: Edit blog, check for image as well.
    02: Reamining forms, bootstrap apply
    03. Add new pages/urls/views to the project as per your need
    04. About => Mention about yourself with your image and signature on it