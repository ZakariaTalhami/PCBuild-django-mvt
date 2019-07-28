from django.contrib import admin
from .models import Comment, Rating
# Register your models here.
models = [
    Comment,
    Rating
]

admin.site.register(models)
