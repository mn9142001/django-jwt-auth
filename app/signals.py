from django.dispatch import receiver
from .models import User
from django.db.models.signals import pre_save
from datetime import datetime

@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, *args, **kwargs):
    if instance._password:
        instance.last_password_change = datetime.now()
    