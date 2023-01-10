from django.urls import path
from . import views
from .views import *

app_name = "profile"

urlpatterns = [

    path('', ProfileDetail, name='profile_detail'),
    path('settings/', ProfileUpdate, name='profile_update'),
]
