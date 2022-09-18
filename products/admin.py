from django.contrib import admin

from products.models import CategoryModel, HouseModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'created_at']
    list_filter = ['created_at']


@admin.register(HouseModel)
class HouseModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'type', 'created_at']
    search_fields = ['title', 'type']
    list_filter = ['created_at']

