import datetime

import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

from apps.mainpage.views import wrong404
from apps.profile.forms import ProfileForm, UserForm, ContactForm
from apps.profile.models import Profile


def email_hash(get_email):
    email = get_email[:int(len(get_email) * 0.2)] + get_email[
                                                    int(len(get_email) * 0.2):-int(len(get_email) * 0.2)].replace(
        get_email[int(len(get_email) * 0.2):-int(len(get_email) * 0.2)],
        '*' * len(get_email[int(len(get_email) * 0.2):-int(len(get_email) * 0.2)])) + get_email[
                                                                                      -int(len(get_email) * 0.2):]
    return email


@login_required
def ProfileDetail(request):
    context = {}
    return render(request, "apps/profile/profile_detail.html", context)


@login_required
@transaction.atomic
def ProfileUpdate(request):
    if request.method == 'POST':

        if User.objects.filter(email=request.POST.get('email')).first():
            if request.user != User.objects.filter(email=request.POST.get('email')).first():
                messages.warning(request, _('Bu e-posta adresiyle bir kullanıcı zaten kayıtlı.'))
                return redirect('profile:profile_update')

        if request.POST.get('tc'):
            if Profile.objects.filter(tc=request.POST.get('tc')).first() and Profile.objects.filter(
                    tc=request.POST.get('tc')).first() != request.user.profile:
                email = Profile.objects.filter(tc=request.POST.get('tc')).first().user.email
                email = email_hash(email)
                messages.warning(request,
                                 'Bu TC numarasına ait bir kullanıcı kayıtlı. Bu TC numarasına ait email adresini ( ' + str(
                                     email) + ' ) kullanarak şifrenizi sıfırlayabilirsiniz.')
                return redirect('profile:profile_update')

        if request.POST.get('accept_terms') is None:
            messages.warning(request, 'Kullanım Sözleşmesi Onaylanmadı.')
            return redirect('profile:profile_update')

        userForm = UserForm(request, request.POST, instance=request.user)
        profileForm = ProfileForm(request, request.POST, request.FILES, instance=request.user.profile)
        contactForm = ContactForm(request, request.POST, instance=request.user.profile)

        if profileForm.is_valid() and userForm.is_valid():
            birthdayStr = datetime.datetime.strptime(request.POST.get('birthday'), '%d.%m.%Y').strftime(
                '%Y-%m-%d')
            birthdayYear = datetime.datetime.strptime(birthdayStr, '%Y-%m-%d').date().year
            urlTc = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?WSDL"
            headers = {'content-type': 'text/xml; charset=utf-8'}
            try:
                if request.POST.get('tc'):
                    body = """<?xml version="1.0" encoding="utf-8"?>
                                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                                  <soap:Body>
                                    <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
                                      <TCKimlikNo>""" + ' '.join(str(request.POST.get('tc')).split()) + """</TCKimlikNo>
                                      <Ad>""" + ' '.join(str(request.POST.get('first_name')).split()) + """</Ad>
                                      <Soyad>""" + ' '.join(str(request.POST.get('last_name')).split()) + """</Soyad>
                                      <DogumYili>""" + ' '.join(str(birthdayYear).split()) + """</DogumYili>
                                    </TCKimlikNoDogrula>
                                  </soap:Body>
                                </soap:Envelope>"""
                    response = requests.post(urlTc, data=body.encode('utf-8'), headers=headers)
                    if 'false' in response.content.decode():
                        messages.warning(request,
                                         _('Girdiğiniz Ad, Soyad, Doğum Tarihi veya Tc Uyuşmamaktadır. '))
                        return redirect('profile:profile_update')
            except Exception as ex:
                print(ex)
                messages.warning(request, _('Bir Hata İle Karşılaşıldı.'))
                return redirect('profile:profile_update')

        if userForm.is_valid() and profileForm.is_valid() and contactForm.is_valid():
            userForm.save()
            profileForm.save()
            contactForm.save()
            messages.success(request, _('Günceleme İşlemi Başarılı'))
            return redirect('profile:profile_update')

        else:
            messages.warning(request, _('Lütfen Formu Eksiksiz Doldurunuz.'))

    else:
        userForm = UserForm(request, instance=request.user)
        profileForm = ProfileForm(request, instance=request.user.profile)
        contactForm = ContactForm(request, instance=request.user.profile)
        context = {
            'userForm': userForm,
            'profileForm': profileForm,
            'contactForm': contactForm,
        }
        return render(request, "apps/profile/profile_update.html", context)
