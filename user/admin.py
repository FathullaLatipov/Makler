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
            'fields': ('pk', 'phone_number', 'is_superuser'),
        }),
    )
    fieldsets = (
        (None, {
            "fields": (
                ('phone_number', 'is_superuser', 'is_staff'),
            ),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
