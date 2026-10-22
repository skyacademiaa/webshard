"""
Core admin configuration.
"""
from django.contrib import admin
from .models import SiteSettings, Slider, Testimonial, WorkProcess


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('اطلاعات کلی', {
            'fields': ('site_name', 'tagline', 'description'),
        }),
        ('لوگو و آیکون', {
            'fields': ('logo', 'logo_dark', 'favicon'),
        }),
        ('اطلاعات تماس', {
            'fields': ('phone_1', 'phone_2', 'email', 'address', 'working_hours'),
        }),
        ('شبکه‌های اجتماعی', {
            'fields': ('instagram', 'telegram', 'whatsapp', 'linkedin', 'twitter', 'github'),
            'classes': ('collapse',),
        }),
        ('سئو', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords', 'og_image'),
            'classes': ('collapse',),
        }),
        ('آنالیتیکس', {
            'fields': ('google_analytics_id',),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        """Only allow one instance."""
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'rating', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active', 'rating')
    search_fields = ('name', 'company')


@admin.register(WorkProcess)
class WorkProcessAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
