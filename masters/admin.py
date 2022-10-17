from django.contrib import admin

from .models import MasterModel, MasterImagesModel, MasterProfessionModel


@admin.register(MasterProfessionModel)
class MasterProfessionModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    search_fields = ['title']
    list_filter = ['title']
    save_on_top = True
    save_as = True


@admin.register(MasterModel)
class MasterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['name', 'email', 'phone']
    save_on_top = True
    save_as = True


@admin.register(MasterImagesModel)
class MasterImagesModel(admin.ModelAdmin):
    list_display = ['pk', 'image']
    save_on_top = True
    save_as = True
