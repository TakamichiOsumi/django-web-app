# django-web-app
django sample project for learning


### How to set up and run

```
$ git clone https://github.com/TakamichiOsumi/ecommerce-web-app.git
$ cd ecommerce-web-app
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ emacs .env
(venv) $ brew services start postgresql
(venv) $ bash pg_setup.sh
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
(venv) $ python manage.py collectstatic
(venv) $ python manage.py runserver
```

### Environment variables required to be defined in .env

* SECRET_KEY
* DEBUG
* ALLOWED_HOSTS
* ADMIN_PATH
* DB_NAME
* DB_USER
* DB_PASSWORD
* DB_HOST
* DB_PORT
* TESTING_DB_NAME
