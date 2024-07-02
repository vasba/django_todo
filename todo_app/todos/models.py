from django.db import models

from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
