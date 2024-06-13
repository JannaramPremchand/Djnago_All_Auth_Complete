from django.urls import path, include
from .views import *
urlpatterns = [
    path('profile/', profile, name='profile'),
]