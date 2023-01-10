import datetime

from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.simple_tag
def static_cdn(url):
    if settings.CDN_ENABLED:
        url = static(url).replace(settings.AWS_S3_CUSTOM_DOMAIN, settings.AWS_S3_CDN_DOMAIN).replace('/static/', '/')
        return url
    else:
        return static(url)


@register.simple_tag
def changelanguage(path, lang):
    if path and lang:
        if lang == 'en':
            newPath = path.replace("/tr/", "/en/")
            newPath = newPath.replace("profil", "profile")

        else:
            newPath = path.replace("/en/", "/tr/")
            newPath = newPath.replace("profile", "profil")
        return newPath
    else:
        return path


@register.filter
def to_br(value):
    return value.replace("<br>", "")


@register.filter
@stringfilter
def custom_date(value):
    now_time = datetime.datetime.now()

    now_time = datetime.datetime.strptime(str(now_time), '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')
    value = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S%z').strftime('%Y-%m-%d %H:%M:%S')

    now_time = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
    value = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=3)

    total_time = now_time - value
    total_time_days = total_time.days
    total_time_str = str(total_time)

    if total_time_days == 1:
        value = str(total_time_days) + " " + _("Gün")
    elif total_time_days < 1:
        value_hour = int(total_time_str.split(':')[0])
        if value_hour == 0:
            value_minute = int(total_time_str.split(':')[1])
            if value_minute == 0:
                value_second = int(total_time_str.split(':')[2])
                value = str(value_second) + " " + _("Saniye")
            else:
                value = str(value_minute) + " " + _("Dakika")
        else:
            value = str(value_hour) + " " + _("Saat")

    elif total_time_days > 1:
        value = value
    else:
        value = value
    return str(value)


custom_date.is_safe = True
