from django.contrib import admin

from products.models import CategoryModel, HouseModel, AmenitiesModel, MasterModel, MasterActivity, MapModel, \
    HouseImageModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'created_at']
    list_filter = ['created_at']


@admin.register(AmenitiesModel)
class AmenitiesModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'created_at']
    list_filter = ['created_at']


@admin.register(MapModel)
class MapModelAdmin(admin.ModelAdmin):
    list_display = ['addressName', 'latitude', 'longtitude', 'created_at']
    search_fields = ['addressName']
    list_filter = ['created_at']

@admin.register(HouseImageModel)
class HouseImageModelAdmin(admin.ModelAdmin):
    list_display = ['image', 'created_at']
    search_fields = ['created_at']
    list_filter = ['created_at']

@admin.register(HouseModel)
class HouseModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'type', 'created_at']
    search_fields = ['title', 'type']
    list_filter = ['created_at']


@admin.register(MasterActivity)
class MasterActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'created_at']
    list_filter = ['title', 'created_at']


@admin.register(MasterModel)
class MasterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['name', 'email', 'phone']
