from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'role',
        'action',
        'method',
        'path',
        'ip_address',
        'timestamp',
    )

    list_filter = (
        'action',
        'role',
        'method',
        'timestamp',
    )

    search_fields = (
        'user__username',
        'path',
        'ip_address',
    )

    readonly_fields = (
        'user',
        'role',
        'action',
        'method',
        'path',
        'ip_address',
        'timestamp',
    )
