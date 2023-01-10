from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext as _
from mptt.models import MPTTModel

from ..common.fileUpload.userPath import userDirectoryPath
from ..common.mixins.audit import AuditMixin
from ..common.oneTextField import OneTextField
from ..common.seo.seo import SeoModel


class SiteSettings(OneTextField):
    site = models.OneToOneField(Site, related_name="settings", on_delete=models.CASCADE, verbose_name='Site')
    copyright = RichTextUploadingField(default="", blank=True, verbose_name=_('copyright'))
    logo = models.ImageField(upload_to=userDirectoryPath, null=True, verbose_name=_('Logo'), blank=True)
    favicon = models.ImageField(upload_to=userDirectoryPath, null=True, verbose_name=_('Fav İcon'), blank=True)
    devremulk_kod = models.ImageField(upload_to=userDirectoryPath, null=True, verbose_name=_('Devremülk Kodları Yatay'),
                                      blank=True)
    devremulk_kod_d = models.ImageField(upload_to=userDirectoryPath, null=True,
                                        verbose_name=_('Devremülk Kodları Dikey'), blank=True)

    @property
    def logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url

    @property
    def favicon_url(self):
        if self.favicon and hasattr(self.favicon, 'url'):
            return self.favicon.url

    @property
    def keywords_list(self):
        my_string = self.seo_keywords
        keywords_list = [x.strip() for x in my_string.split(',')]

        return keywords_list

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Site Ayarları'
        verbose_name_plural = 'Site Ayarları'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Icon(OneTextField):
    class Meta:
        verbose_name = 'İcon'
        verbose_name_plural = 'İcon'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class MenuType(OneTextField):

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Menü Tipi'
        verbose_name_plural = 'Menü Tipi'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Menu(MPTTModel):
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.CASCADE,
                               verbose_name='Üst Menü')
    menu_type = models.ForeignKey(MenuType, blank=True, on_delete=models.PROTECT, null=True,
                                  verbose_name='Menü Tipi')
    icon = models.ForeignKey(Icon, blank=True, on_delete=models.PROTECT, null=True, verbose_name='İcon')
    name = models.CharField(max_length=250, verbose_name='Başlık')
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name="Link")
    alignment = models.IntegerField(null=True, blank=True, verbose_name='Sıralama')
    groupList = models.ManyToManyField(Group, blank=True, verbose_name="Grup")

    def __str__(self):
        if self.menu_type:
            return str(self.name) + " | " + str(self.menu_type.text)
        else:
            return str(self.name)

    class Meta:
        verbose_name = 'Menü'
        verbose_name_plural = 'Menü'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
