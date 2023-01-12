from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.common.oneTextField import OneTextField


class TrainingUser(OneTextField):
    user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, null=True, verbose_name='Kullanıcı')
    set = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Set Sayısı'))
    antrenman = RichTextUploadingField(default="", blank=True, verbose_name=_('Antrenman Açıklaması'))
    active = models.BooleanField(blank=True, null=True, default=False, verbose_name='Durumu')

    class Meta:
        verbose_name = 'Eğitimler'
        verbose_name_plural = 'Eğitimler'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
