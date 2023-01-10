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

BOOL_CHOICES = ((True, _('Evet')), (False, _('Hayır')))


class Profile(AuditMixin):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name=_('Kullanıcı'))

    profile_image = models.ImageField(upload_to=userDirectoryPath, validators=[validateFileExtensionPhoto], blank=True,
                                      null=True, verbose_name=_('Profil Resmi'))

    tc = models.BigIntegerField(null=True, unique=True, blank=True, verbose_name=_('T.C. Kimlik Numarası'))

    birthdayRegex = RegexValidator(
        regex=r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$',
        message="Lütfen doğru formatta giriniz: 'gg.aa.yyyy' ")

    birthday = models.CharField(validators=[birthdayRegex], max_length=15, null=True, verbose_name=_('Doğum Tarihi'))

    phoneNumberRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                      message=_("Lütfen doğru formatta giriniz: '+901234567890' "))

    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=15, null=True, blank=True,
                                   verbose_name=_('Cep Telefonu'))

    address = models.TextField(null=True, blank=True, verbose_name=_('Adres'))

    max_credit = models.IntegerField(default=100, null=True, verbose_name=_('Kredi Üst Uyarı Limiti'))

    slug = models.SlugField(max_length=500, null=True, blank=True, editable=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(str(int(self.user.id) + 1000))
        super(Profile, self).save(*args, **kwargs)

    @property
    def get_profile_image_url(self):
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image
        else:
            return SiteSettings.objects.first().default_profile_image

    def get_credit_percent(self):
        credit = self.get_credit()
        if self.max_credit > 0:
            data = ((credit * 100) // self.max_credit)
        else:
            data = 0
        if data > 100:
            data = 100

        return data

    class Meta:
        verbose_name = _('Profil')
        verbose_name_plural = _('Profil')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))

