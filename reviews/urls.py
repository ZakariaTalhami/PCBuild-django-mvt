from django.urls import path
from . import views

urlpatterns = [
    path('comment/submit', views.CommentCreateView.as_view(), name='comment-create')
]