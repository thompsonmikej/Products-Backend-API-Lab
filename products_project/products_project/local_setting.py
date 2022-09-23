# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@i-e9s2ai=l1awricgpjz)#y!lx^h@=yoxuwb_gby#avmzrdf("

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "mysql.connector.django",
        "NAME": 'products_project',
        'HOST': '127.0.0.1',
        'PORT': '3306'
        'USER': 'root',
        'PASSWORD': 'password',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
