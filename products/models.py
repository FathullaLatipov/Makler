from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField


class CategoryModel(models.Model):
    title = models.CharField(max_length=500, verbose_name=_('title'))
    image = models.FileField(upload_to='category_image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class AmenitiesModel(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('All_amenities')
        verbose_name_plural = _('All_amenities')


class MapModel(models.Model):
    addressName = models.CharField(max_length=200, verbose_name=_('address'))
    latitude = models.FloatField(verbose_name=_('latitude'))
    longtitude = models.FloatField(verbose_name=_('longtitude'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.addressName

    class Meta:
        verbose_name = _('Map')
        verbose_name_plural = _('Maps')


class HouseImageModel(models.Model):
    image = models.FileField(upload_to='house_images', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = _('house_image')
        verbose_name_plural = _('house_images')


class HouseModel(models.Model):
    title = models.CharField(max_length=600, verbose_name=_('title'))
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name=_('category'),
                                 related_name=_('category'), null=True
                                 )
    descriptions = models.TextField(verbose_name=_('descriptions'))
    price = models.CharField(max_length=100, verbose_name=_('price'))
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
    image = models.ManyToManyField(HouseImageModel, verbose_name=_('image'))
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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('House')
        verbose_name_plural = _('Houses')
