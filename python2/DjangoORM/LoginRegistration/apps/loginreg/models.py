from __future__ import unicode_literals

from django.db import models
import re
regex_obj = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


# Create your models here.
class RegistrationManager(models.Manager):
    def regval(self, data):
        errors = []
        if len(data['first_name']) < 2 or len(data['last_name']) < 2:
            errors.append('First and last name must be at least 2 characters.')
        if not regex_obj.match(data['email']):
            errors.append('Please enter a valid email address')
        if len(data['password']) < 8 or data['password'] != data['confirmpw']:
            errors.append('Password must be at least 8 characters long and match')
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = RegistrationManager()