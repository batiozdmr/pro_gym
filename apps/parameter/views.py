from django.shortcuts import render
from apps.training.models import *


def accounts(request):
    users = User.objects.all()
    return render(request, "account/account_list.html", {'users': users})
