"""
Services admin configuration.
"""
from django.contrib import admin
from .models import Service, ServiceFeature


class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceFeatureInline]

    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'slug', 'short_description', 'description', 'icon', 'cover'),
        }),
        ('تنظیمات', {
            'fields': ('order', 'is_active'),
        }),
        ('سئو', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
        }),
    )
