from django.urls import path
from . import views

urlpatterns = [
    path('build', views.BuildList.as_view(), name="build-list"),
    path('build/<int:pk>', views.BuildDetail.as_view(), name="build-detail"),
]