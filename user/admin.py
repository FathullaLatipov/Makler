from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['pk', 'phone_number', 'created_at',]
    ordering = ['pk',]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('pk', 'phone_number',),
        }),
    )
    fieldsets = (
        (None, {
            "fields": (
                ('phone_number',),
            ),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
