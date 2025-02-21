from django.urls import path
from .views import download_video

urlpatterns = [
    path("downloads", download_video, name="download")
]
from .views import home

urlpatterns = [
    path('', home, name="home"),
    path("download/", download_video, name="download"),
]
