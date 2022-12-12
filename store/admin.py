from django.contrib import admin

from store.models import StoreModel, StoreAmenities, UseForModel


@admin.register(StoreAmenities)
class StoreAmenities(admin.ModelAdmin):
    list_display = ['title', 'created_at']


@admin.register(UseForModel)
class UseForModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


@admin.register(StoreModel)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'phoneNumber', 'created_at']
    search_fields = ['pk', 'name', 'phoneNumber']
    list_filter = ['name', 'created_at']
    save_on_top = True
    save_as = True
