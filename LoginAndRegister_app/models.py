from django.db import models
import re
from time import gmtime, strftime, time
# create the validation manager for our mTVShow model
class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['firstName']) <2:
            errors['firstName'] = "The First Name Should be atleast 2 characters"
        if len(postData['LastName']) <3:
            errors['LastName'] = "The LastName  Should be atleast 3 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = "Invalid email address!"
        if postData['Pass'] !=  postData['confirmPass']:
            errors['confirm'] = "The Passwords do not match!"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True )
    objects = UsersManager()

# Create your models here.
