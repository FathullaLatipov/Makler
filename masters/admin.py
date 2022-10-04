from django.contrib import admin

from .models import MasterModel, MasterImagesModel, MasterProfessionModel


@admin.register(MasterModel)
class MasterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['name', 'email', 'phone']


admin.site.register(MasterImagesModel)
admin.site.register(MasterProfessionModel)
