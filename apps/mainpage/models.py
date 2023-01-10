from django.utils.translation import gettext_lazy as _

from apps.common.oneTextField import OneTextField


class MainPage(OneTextField):

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Ana Sayfa'
        verbose_name_plural = 'Ana Sayfa'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
