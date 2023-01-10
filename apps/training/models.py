from autoslug.settings import slugify
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.common.fileUpload.userPath import userDirectoryPath
from apps.common.fileUpload.validate import validateFileExtensionPhoto
from apps.common.mixins import AuditMixin
from apps.common.oneTextField import OneTextField
from apps.parameter.models import SiteSettings
from django.core.validators import MinValueValidator
from decimal import Decimal


class InterviewStatus(OneTextField):
    class Meta:
        verbose_name = 'Görüşme Durumu'
        verbose_name_plural = 'Görüşme Durumu'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Community(AuditMixin):
    phoneNumberRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                      message=_("Lütfen doğru formatta giriniz: '+901234567890' "))

    block = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Blok'))
    entrance = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Giriş'))
    apartment = models.IntegerField(blank=True, null=True, verbose_name=_('Daire'))
    period = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Dönem'))
    period_code = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Dönem Kodu'))
    m2 = models.IntegerField(blank=True, null=True, verbose_name=_('m2'))
    full_name = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Ad Soyad'))
    phone_one = models.CharField(validators=[phoneNumberRegex], max_length=15, blank=True, null=True,
                                 verbose_name=_('Telefon 1'))
    phone_two = models.CharField(validators=[phoneNumberRegex], max_length=15, blank=True, null=True,
                                 verbose_name=_('Telefon 2'))
    phone_three = models.CharField(validators=[phoneNumberRegex], max_length=15, blank=True, null=True,
                                   verbose_name=_('Telefon 3'))
    tc = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('TC'))
    circuit_start = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Devre Başlangıç'))
    circuit_finish = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Devre Bitiş'))

    def __str__(self):
        return self.period_code

    def interview_list(self):
        data = Interview.objects.filter(community=self).order_by('-id')
        return data

    def interview_last(self):
        data = Interview.objects.filter(community=self).last()
        return data

    class Meta:
        verbose_name = 'Topluluk'
        verbose_name_plural = 'Topluluk'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Interview(AuditMixin):
    community = models.ForeignKey(Community, related_name="interview_community", on_delete=models.CASCADE,
                                  verbose_name='Topluluk')
    user = models.ForeignKey(User, related_name="interview_user", on_delete=models.CASCADE, verbose_name='Kullanıcı')
    note = models.TextField(null=True, blank=True, verbose_name='Not')
    interview_status = models.ForeignKey(InterviewStatus, null=True, blank=True,
                                         related_name="interview_interview_status",
                                         on_delete=models.CASCADE, verbose_name='Durum')
    price_sales = models.DecimalField(default=0.00, verbose_name=_("Satış Fiyatı"), help_text=_("Minimum 0.00"),
                                      max_digits=19, decimal_places=2,
                                      validators=[MinValueValidator(Decimal('0.00'))], )

    price_rent = models.DecimalField(default=0.00, verbose_name=_("Kira Ücreti"), help_text=_("Minimum 0.00"),
                                     max_digits=19, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], )

    def __str__(self):
        return str(self.community.period_code)

    class Meta:
        verbose_name = 'Görüşme'
        verbose_name_plural = 'Görüşme'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
