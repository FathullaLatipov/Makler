from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

from user.models import CustomUser


class CategoryModel(models.Model):
    title = models.CharField(max_length=500, verbose_name=_('title'))
    image = models.FileField(upload_to='category_image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class AmenitiesModel(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'))
    image = models.FileField(upload_to='amenities_images')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Все удобства')
        verbose_name_plural = _('Все удобства')


class MapModel(models.Model):
    addressName = models.CharField(max_length=200, verbose_name=_('address'))
    latitude = models.FloatField(verbose_name=_('latitude'))
    longtitude = models.FloatField(verbose_name=_('longtitude'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.addressName

    class Meta:
        verbose_name = _('Карта')
        verbose_name_plural = _('Карты')


class ImagesModel(models.Model):
    image = models.FileField(upload_to='house_test_image', null=True)

    def __str__(self):
        return f"127.0.0.1:7783{self.image.url}"


class PriceListModel(models.Model):
    price = models.CharField(max_length=10, verbose_name=_('price'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.price

    class Meta:
        verbose_name = _('Цена')
        verbose_name_plural = _('Цены')


class HouseModel(models.Model):
    creator = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='houses', null=True,
                                blank=True)
    title = models.CharField(max_length=600, verbose_name=_('title'))
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name=_('category'),
                                 related_name=_('category'), null=True, blank=True
                                 )
    descriptions = models.TextField(verbose_name=_('descriptions'))
    price = models.CharField(max_length=100, verbose_name=_('price'))
    price_type = models.ForeignKey(PriceListModel, on_delete=models.CASCADE, related_name='price_types')
    ADD_TYPE = (
        ('rent', 'Rent'),
        ('for_sale', 'For_sale'),
    )
    type = models.CharField(
        max_length=200,
        choices=ADD_TYPE,
        default=ADD_TYPE[1],
        null=True,
        blank=True,
    )
    web_type = models.CharField(max_length=400, verbose_name=_('web_type'), null=True)
    web_rental_type = models.CharField(max_length=500, verbose_name=_('web_rental_type'), null=True)
    web_object = models.CharField(max_length=300, verbose_name=_('web_object'), null=True)
    web_building_type = models.CharField(max_length=600, verbose_name=_('web_building_type'), null=True)
    RENTAL_TYPE = (
        ('long_time', 'Long_time'),
        ('several_months', 'Several_months'),
        ('daily', 'Daily')
    )
    rental_type = models.CharField(
        max_length=200,
        choices=RENTAL_TYPE,
        default=RENTAL_TYPE[1],
        null=True,
        blank=True,
    )
    PROPERTY_TYPE = (
        ('residential', 'Residential'),
        ('commercial', 'Commercial')
    )
    OBJECT = (
        ('flat', 'Flat'),
        ('room', 'Room'),
        ('summer_cottage', 'Summer_cottage'),
        ('house', 'House'),
        ('part_house', 'Part_house'),
        ('townhouse', 'Townhouse'),
        ('bed_space', 'Bed_space')
    )
    object = models.CharField(
        max_length=200,
        choices=OBJECT,
        default=None,
        null=True,
        blank=True,
    )
    address = models.ForeignKey(MapModel, on_delete=models.CASCADE, verbose_name=_('address'), null=True)
    # images = models.ManyToManyField(ImagesModel, null=True, blank=True)
    general = models.CharField(max_length=90, verbose_name=_('general'))
    residential = models.CharField(max_length=90, verbose_name=_('residential'))
    number_of_rooms = models.CharField(max_length=30, verbose_name=_('number_of_rooms'))
    floor = models.CharField(max_length=30, verbose_name=_('floor'))
    floor_from = models.CharField(max_length=30, verbose_name=_('floor_from'))
    BUILDING_TYPE = (
        ('brick', 'Brick'),
        ('monolith', 'Monolith'),
        ('panel', 'Panel'),
        ('blocky', 'Blocky')
    )
    building_type = models.CharField(
        max_length=50,
        choices=BUILDING_TYPE,
        default=None,
        verbose_name=_('building_type'),
        null=True,
        blank=True,
    )
    amenities = models.ManyToManyField(AmenitiesModel, verbose_name=_('amenities'), blank=True)
    isBookmarked = models.BooleanField(default=False, verbose_name=_('isBookmarked'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    draft = models.BooleanField(default=False)
    PRODUCT_STATUS = (
        ('InProgress', 'InProgress'),
        ('PUBLISH', 'PUBLISH'),
        ('DELETED', 'DELETED'),
        ('ARCHIVED', 'ARCHIVED'),
        ('REJECTED', 'REJECTED')
    )
    product_status = models.CharField(
        choices=PRODUCT_STATUS,
        default=PRODUCT_STATUS[0],
        max_length=30,
        null=True
    )

    def __str__(self):
        return self.title

    @staticmethod
    def get_from_wishlist(request):
        wishlist = request.session.get('wishlist', [])
        return HouseModel.objects.filter(pk__in=wishlist)

    # @property
    # def choices(self):
    #     return [{'rental_type': self.rental_type}, ['object', self.object], ['building_type', self.building_type]]

    class Meta:
        verbose_name = _('Маклер, (квартиры и т.д)')
        verbose_name_plural = _('Маклер, (квартиры и т.д)')
        ordering = ['-id']


class NewHouseImages(models.Model):
    product = models.ForeignKey(HouseModel, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='API/images', max_length=100, null=True)


class HouseImageModel(models.Model):
    property_id = models.ForeignKey(HouseModel, null=False, default=1, on_delete=models.CASCADE,
                                    related_name='pr_images')
    image = models.ImageField(upload_to='house_images', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = _('Изображения маклер (квартиры и т.д)')
        verbose_name_plural = _('Изображения маклер (квартиры и т.д)')

#
# class HouseOptionsModel(models.Model):
#     product = models.ForeignKey(HouseModel, on_delete=models.PROTECT, related_name='products_options',
#                                 verbose_name=_('product'), null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = _('product_options')
#         verbose_name_plural = _('product_options')
