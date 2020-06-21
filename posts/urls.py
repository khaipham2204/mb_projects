from django.urls import path, include
from .views import HomePageVieww
urlpatterns = [
    path('', HomePageVieww.as_view(), name='home')
]
