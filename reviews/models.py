from django.db import models
from users.models import CustomUser
from parts.models import Part
# Create your models here.

class Review(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        unique_together = ['part', 'owner']

class Rating(Review):
    Rating = models.FloatField()

class Comment(Review):
    text = models.CharField(max_length=512)


 