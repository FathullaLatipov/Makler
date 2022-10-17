from django.db import models
from django.utils.translation import gettext_lazy as _


class StoreModel(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    description = models.TextField()
    image = models.FileField(upload_to='store_images', verbose_name=_('image'))
    brand_image = models.FileField(upload_to='avatar_image', verbose_name=_('brand_image'), null=True)
    brand = models.CharField(max_length=200, verbose_name=_('brand'), null=True)
    price = models.PositiveIntegerField(verbose_name=_('price'), null=True)
    use_for = models.CharField(max_length=400, verbose_name=_('use_for'), null=True)
    phoneNumber = models.PositiveIntegerField(verbose_name=_('phoneNumber'))
    address = models.CharField(max_length=400, verbose_name=_('address'), null=True)
    email = models.EmailField(verbose_name=_('email'))
    isBookmarked = models.BooleanField(default=False, verbose_name=_('isBookmarked'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    @staticmethod
    def get_from_wishlist(request):
        wishlist = request.session.get('wishlist', [])
        return StoreModel.objects.filter(pk__in=wishlist)

    class Meta:
        verbose_name = _('Store')
        verbose_name_plural = _('Stores')
