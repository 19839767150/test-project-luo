from django.test import TestCase

# Create your tests here.
import os
import django
import datetime

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobook.settings')
    django.setup()

    from app01 import models
    res = models.Book.objects.filter(pk=2).first()

    print(res.publish_id)
