import os
from urllib import request

import openpyxl
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_asgi_application()

from apps.training.models import Community, Interview


def excel_read(request):
    community_list = Community.objects.filter()
    for community in community_list:
        interview = Interview.objects.filter(community=community).last()
        if interview:
            if interview.interview_status:
                community.interview_status = interview.interview_status
                community.save()
                print("Eklendi")
            else:
                print("Hata1 : " + str(community.id))
        else:
            print("Hata2 : " + str(community.id))


excel_read(request)
