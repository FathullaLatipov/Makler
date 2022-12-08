from django.db import models
from django.utils.translation import gettext_lazy as _


class MasterProfessionModel(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Профессия')
        verbose_name_plural = _('Профессии')




class MasterModel(models.Model):
    owner = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='maklers', null=True)
    name = models.CharField(max_length=100, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.PositiveIntegerField(verbose_name=_('phone'))
    password = models.CharField(verbose_name=_('password'), max_length=100)
    # address = models.ForeignKey(MapModel, on_delete=models.CASCADE, verbose_name=_('address'),
    #                             related_name='address', null=True)
    address_title = models.CharField(max_length=300, verbose_name=_('address_title'), null=True)
    address_latitude = models.FloatField(max_length=90, verbose_name=_('address_latitude'), null=True)
    address_longitude = models.FloatField(max_length=90, verbose_name=_('address_longitude'), null=True)
    avatar = models.FileField(upload_to='master_avatar', verbose_name=_('avatar'))
    profession = models.ManyToManyField(MasterProfessionModel, verbose_name=_('profession'),
                                        related_name='profession', blank=True
                                        )
    descriptions = models.TextField(verbose_name=_('descriptions'))
    experience = models.IntegerField(verbose_name=_('experience'), null=True)
    isBookmarked = models.BooleanField(default=False, verbose_name=_('isBookmarked'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    draft = models.BooleanField(default=False)
    PRODUCT_STATUS = [
        (0, 'InProgress'),
        (1, 'PUBLISH'),
        (2, 'DELETED'),
        (3, 'ARCHIVED'),
        (4, 'REJECTED'),
    ]
    product_status = models.IntegerField(
        choices=PRODUCT_STATUS,
        default=0,
        null=True
    )

    def __str__(self):
        return self.name

    @staticmethod
    def get_from_wishlist(request):
        wishlist = request.session.get('wishlist', [])
        return MasterModel.objects.filter(pk__in=wishlist)

    class Meta:
        verbose_name = _('Мастер')
        verbose_name_plural = _('Мастеры')
        ordering = ['-id']


class MasterImagesModel(models.Model):
    master = models.ForeignKey(MasterModel, on_delete=models.CASCADE, related_name='images')
    images = models.FileField(upload_to='master_images', max_length=100, null=True)

    class Meta:
        verbose_name = _('Изображения для мастера')
        verbose_name_plural = _('Изображения для мастеров')
