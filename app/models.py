from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    last_password_change = models.DateTimeField(auto_now_add=True)