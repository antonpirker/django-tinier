# django-tinier

A template for a Django project with a flatter directory structure.


## Setting up virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## Running the application

### Development server:

```bash
cd mysite
python manage.py runserver 8000
```

### Gunicorn:
```bash
cd mysite
gunicorn wsgi:application
```

### Uvicorn:
```bash
uvicorn asgi:application
```
