from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(unique=True, null=True, blank=True)