CSUA-backend
============

A backend for the CSUA interblags.

## Getting started

1. Install Python 2
2. Install Django with `pip install -r requirements.txt` (Consider using `--user` flag)
3. Change `DEBUG` to `True` at the top of `csua_backend/settings.py`
4. Create database file with `mkdir data` and `touch data/csua.sqlite3`
5. Set up local db with `python2 manage.py migrate`
6. Run server with `python2 manage.py runserver`
7. Navigate to http://127.0.0.1:8000/

If you want to visit the admin page at http://127.0.0.1:8000/admin/

8. Create admin user with `python2 manage.py createsuperuser`

## Deploy a new change to git

1. `ssh` into `services.csua`
2. `git pull`
3. `python manage.py collectstatic` to update static images
4. If you're making changes to the db models, follow those instructions too

## Making changes to database models

1. Make changes to `db_data/models.py`
2. `python manage.py makemigrations` on your development machine
3. `python manage.py migrate` to apply new migrations to your local db
4. Commit and push your changes to `models.py` as well as generated `migrations/`
5. Pull latest changes on remote machine
6. `python manage.py migrate` on remote machine to update database with latest models

## Editing/Creating/Deleting Officers

Go to csua.berkeley.edu/admin/ to edit officer data!
