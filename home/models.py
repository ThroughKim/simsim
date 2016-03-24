from django.db import models

# Create your models here.

class Conversation(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    ask = models.TextField(default=None, null=True, blank=True)
    answer = models.TextField(default=None, null=True, blank=True)