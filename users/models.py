from django.db import models
from django.contrib.auth.models import User


class UserMessages(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.DO_NOTHING)
    recipient = models.ForeignKey(User, related_name='recipient', on_delete=models.DO_NOTHING)
    msg = models.CharField(max_length=500)
