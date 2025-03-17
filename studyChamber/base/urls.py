from django.urls import path
from . import views

urlpatterns = [
    path('',view.home,name=home),
    path('room/',view.room,name=room),
]