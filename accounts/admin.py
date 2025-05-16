from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name',
                    'last_name', 'mobile', 'email', 'is_active']
    search_fields = ['username']

    def delete_queryset(self, request, queryset):
        for user in queryset:
            user.delete()
