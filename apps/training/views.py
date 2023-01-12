from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _

from apps.training.models import TrainingUser


@login_required
def form(request, id):
    TrainingUser.objects.filter(id=id).update(
        active=True
    )
    messages.success(request, _("Antrenman Tamamlandı"))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
