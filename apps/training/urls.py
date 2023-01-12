from django.urls import path

from .views import *

app_name = "training"

urlpatterns = [
    path('form/<int:id>/', form, name='form'),

]
