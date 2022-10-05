from django.db import models
from LoginAndRegister_app.models import *

class Messages(models.Model):
    message = models.CharField (max_length = 255)
    user_id = models.ForeignKey(Users, related_name="messages", on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True )

class Comments(models.Model):
    comment = models.CharField (max_length = 255)
    user_id = models.ForeignKey(Users, related_name="comments", on_delete = models.DO_NOTHING)
    message_id = models.ForeignKey(Messages, related_name="messageComments", on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True )
# Create your models here.
