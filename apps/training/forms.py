from django import forms
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _

from apps.training.models import *


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ('interview_status', 'price_sales', 'price_rent', 'note')

    def __init__(self, request, *args, **kwargs):
        super(InterviewForm, self).__init__(*args, **kwargs)
        self.fields['interview_status'].choices = [(t.id, t.text) for t in InterviewStatus.objects.all()]
