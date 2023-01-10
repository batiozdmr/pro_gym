from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.shortcuts import render


@login_required
def index(request):
    context = {
    }
    return render(request, "index.html", context)


def file(request):
    context = {

    }
    return render(request, "file.html", context)


def wrong403(request):
    return render(request, "404.html")


def wrong404(request):
    return render(request, "404.html")


def wrong500(request):
    return render(request, "404.html")
