"""
Quote admin configuration.
"""
from django.contrib import admin
from .models import ProjectQuote


@admin.register(ProjectQuote)
class ProjectQuoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'project_type', 'budget_range', 'status', 'created_at')
    list_editable = ('status',)
    list_filter = ('status', 'project_type', 'budget_range', 'created_at')
    search_fields = ('name', 'company', 'phone', 'email', 'description')
    readonly_fields = ('name', 'company', 'phone', 'email', 'project_type',
                       'budget_range', 'timeline', 'description', 'reference_url', 'created_at')
    date_hierarchy = 'created_at'

    fieldsets = (
        ('اطلاعات مشتری', {
            'fields': ('name', 'company', 'phone', 'email'),
        }),
        ('جزئیات پروژه', {
            'fields': ('project_type', 'budget_range', 'timeline', 'description', 'reference_url'),
        }),
        ('مدیریت', {
            'fields': ('status', 'admin_notes'),
        }),
        ('تاریخ', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        return False
