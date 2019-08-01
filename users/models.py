from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.CharField(max_length=1024, null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name="to_user")
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name="from_user")