from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import MapModel


class MasterProfessionModel(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('profession')
        verbose_name_plural = _('professions')


class MasterImagesModel(models.Model):
    image = models.FileField(upload_to='master_images', verbose_name=_('image'))

    class Meta:
        verbose_name = _('master_image')
        verbose_name_plural = _('master_images')


class MasterModel(models.Model):
    image = models.FileField(upload_to='master_image', verbose_name=_('image'))
    name = models.CharField(max_length=100, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.PositiveIntegerField(verbose_name=_('phone'))
    password = models.CharField(verbose_name=_('password'), max_length=100)
    address = models.ForeignKey(MapModel, on_delete=models.CASCADE, verbose_name=_('address'),
                                related_name='address', null=True)
    avatar = models.FileField(upload_to='master_avatar', verbose_name=_('avatar'))
    profession = models.ManyToManyField(MasterProfessionModel, verbose_name=_('profession'),
                                        related_name='profession', blank=True
                                        )
    images = models.ManyToManyField(MasterImagesModel, verbose_name=_('images'), related_name='images', blank=True)
    descriptions = models.TextField(verbose_name=_('descriptions'))
    experience = models.IntegerField(verbose_name=_('experience'), null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
