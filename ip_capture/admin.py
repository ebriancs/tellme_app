from django.contrib import admin
from .models import UserDetail

class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_address', 'latitude', 'longitude', 'timestamp')
    search_fields = ('ip_address',)
    list_filter = ('timestamp',)

    readonly_fields = ('id', 'ip_address', 'latitude', 'longitude', 'timestamp')
    fieldsets = (
        (None, {
            'fields': ('id', 'ip_address', 'latitude', 'longitude', 'device_info', 'timestamp'),
        }),
    )

admin.site.register(UserDetail, UserDetailAdmin)
