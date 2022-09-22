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


class HouseModel(models.Model):
    title = models.CharField(max_length=600, verbose_name=_('title'))
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name=_('category'))
    descriptions = models.TextField(verbose_name=_('descriptions'))
    price = models.PositiveIntegerField()
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

    map = models.CharField(max_length=190, verbose_name=_('map'))
    image = models.FileField(upload_to='house_image', verbose_name=_('image'))
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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('House')
        verbose_name_plural = _('Houses')