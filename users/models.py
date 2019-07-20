from django.db import models
from django.contrib.auth.models import AbstractUser
from builds.models import PcBuild

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.CharField(max_length=1024)
    builds = models.ManyToManyField(PcBuild, blank=True, related_name='%(class)s_builds')
    likes = models.ManyToManyField(PcBuild, blank=True, related_name="%(class)s_liked_builds")
    followers = models.ManyToManyField('self', blank=True)
    following = models.ManyToManyField('self', blank=True)