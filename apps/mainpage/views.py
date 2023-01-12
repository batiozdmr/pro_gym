from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.training.models import TrainingUser


@login_required
def index(request):
    training_list = TrainingUser.objects.filter(user=request.user, active=False)
    context = {
        'training_list': training_list
    }
    return render(request, "index.html", context)


def taksit(request):
    context = {

    }
    return render(request, "apps/taksit.html", context)


def qr(request):
    context = {

    }
    return render(request, "apps/qr.html", context)


def wrong403(request):
    return render(request, "404.html")


def wrong404(request):
    return render(request, "404.html")


def wrong500(request):
    return render(request, "404.html")
