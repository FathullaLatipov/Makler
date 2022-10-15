from django.db import models
from django.utils.translation import gettext_lazy as _


class StoreModel(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    description = models.TextField()
    image = models.FileField(upload_to='store_images', verbose_name=_('image'))
    phoneNumber = models.PositiveIntegerField(verbose_name=_('phoneNumber'))
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
