# SALES OVERVIEW PROJECT
## Description
```commandline
This application is designed to obtain sales data. 
It implements the following technologies: 
- Django Rest Framwork
- Database models and normalization
- MySQL
- Celery
- env, requirements.txt
- Swagger
- Git (commits, PR, gitignore, README)
```

## Сommands to run application
```commandline
>>>> fpip install -r requirements.txt
>>>> python manage.py runserver
```

## Сommands to run celery
```commandline
>>>> python -m celery -A sales_overview_project worker -l info -P gevent
>>>> celery -A sales_overview_project beat -l info
```

## Сommands to run migrations
```commandline
>>>> python manage.py makemigrations
>>>> python manage.py migrate
```
