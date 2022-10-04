from django.contrib import admin

from .models import MasterModel, MasterImagesModel, MasterProfessionModel


@admin.register(MasterModel)
class MasterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['name', 'email', 'phone']


@admin.register(MasterImagesModel)
class MasterImagesModel(admin.ModelAdmin):
    list_display = ['pk', 'image']
