from django.urls import path
from . import views


urlpatterns = [
    path('cpu', views.CpuListView.as_view(), name="parts-cpu-list"),
    path('cpu/create', views.CpuCreate.as_view(), name="parts-cpu-create"),
    path('cpu/<int:pk>', views.CpuDetailView.as_view(), name="parts-cpu-detail"),
    path('memory', views.MemoryListView.as_view(), name="parts-memory-list"),
    path('memory/<int:pk>', views.MemoryDetailView.as_view(), name="parts-memory-detail"),
    path('mobo', views.MoboListView.as_view(), name="parts-mobo-list"),
    path('mobo/<int:pk>', views.MoboDetailView.as_view(), name="parts-mobo-detail"),
    path('storage', views.StorageListView.as_view(), name="parts-storage-list"),
    path('storage/<int:pk>', views.StorageDetailView.as_view(), name="parts-storage-detail"),
    path('videocard', views.VideocardListView.as_view(), name="parts-videocard-list"),
    path('videocard/<int:pk>', views.VideocardDetailView.as_view(), name="parts-videocard-detail"),
]