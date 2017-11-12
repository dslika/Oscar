from settings import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'oscar_travis',
        'USER': 'travis',
        'PASSWORD': 'travistest',
        'HOST': 'aa1m867aujcesl7.ckvvuj6ic3ie.ap-northeast-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
