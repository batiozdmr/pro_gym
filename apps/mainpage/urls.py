from django.urls import path

from .views import *

app_name = "mainpage"

urlpatterns = [
    path('', index, name='index'),
    path('taksit/', taksit, name='taksit'),
    path('qr-cod/', qr, name='qr'),

]
