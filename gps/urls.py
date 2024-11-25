from .views import GpsView
from django.urls import path

urlpatterns = [
    path("gps/", GpsView.as_view())
]