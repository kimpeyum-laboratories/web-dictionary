# Kimpeyüm Web Dictionary
## Getting Started
### Dependencies
* Python 3.12+
* Django 5.2
### Local Development
Before starting the local development server, you must first install the project dependencies.
```
pip install -r requirements.txt
```
Then, you shall prepare the local database by creating migrations...
```
python3 manage.py makemigrations
```
...and applying them.
```
python3 manage.py migrate
```
Optionally, if you need to access the Django Admin panel, you can create a superuser account.
```
python3 manage.py createsuperuser
```
Finally, launch the local development server.
```
python3 manage.py runserver
```