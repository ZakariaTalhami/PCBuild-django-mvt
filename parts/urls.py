from django.urls import path
from . import views


urlpatterns = [
    path('cpu', views.CpuList.as_view(), name="parts:cpu-list"),
    path('cpu/<int:pk>', views.CpuDetail.as_view(), name="parts:cpu-detail"),
    path('memory', views.MemoryList.as_view(), name="parts:memory-list"),
    path('memory/<int:pk>', views.MemoryDetail.as_view(), name="parts:memory-detail"),
    path('mobo', views.MoboList.as_view(), name="parts:mobo-list"),
    path('mobo/<int:pk>', views.MoboDetail.as_view(), name="parts:mobo-detail"),
    path('storage', views.StorageList.as_view(), name="parts:storage-list"),
    path('storage/<int:pk>', views.StorageDetail.as_view(), name="parts:storage-detail"),
    path('videocard', views.VideocardList.as_view(), name="parts:videocard-list"),
    path('videocard/<int:pk>', views.VideocardDetail.as_view(), name="parts:videocard-detail"),
]