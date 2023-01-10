from django.urls import path
from .views import *

app_name = "parameter"

urlpatterns = [
    path('account/', accounts, name='account'),

]
