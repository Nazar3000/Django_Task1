A small, working Django site that serves a simple activity feed list with 3 filters:
-My posts
-Me and the posts of everyone I’m tracking (note: use an asymmetric relationship, meaning, “Even if I track you, you may or may not track me”.)
-Everybody’s posts

The project requires Postgresql and Python3 to be installed

**Startup steps:**

1.RUN: sudo -i -u postgres
2.RUN: createuser django_task1 -P
3.RUN: createdb django_task1db --owner django_task1
4.At the root of the project RUN: pip install -r requirements.txt
4.RUN: python manage.py makemigrations
5.RUN: python manage.py migrate
6.RUN: python manage.py createsuperuser --username='Your name' --email='your email'
7.RUN: python manage.py runserver
8.Log in and enjoy

