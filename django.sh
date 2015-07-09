#install django


# start a project
django-admin.py startproject xxx


# migrate database schema
python manage.py migrate

python manage.py runserver
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8000


[Tutorial 1]
python manage.py startapp polls
python manage.py makemigrations polls

produce polls/migrations/0001_initial.py
python manage.py sqlmigrate polls 0001

[Tutorial 2]
#Creating an admin user
python manage.py createsuperuser                                                


# migrate database schema
python manage.py migrate

python manage.py runserver
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8000


[Tutorial 1]
python manage.py startapp polls
python manage.py makemigrations polls

produce polls/migrations/0001_initial.py
python manage.py sqlmigrate polls 0001

[Tutorial 2]
#Creating an admin user
python manage.py createsuperuser                                                


