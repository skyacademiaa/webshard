"""
Pricing admin configuration.
"""
from django.contrib import admin
from .models import PricingCategory, PricingModule, PricingPreset


class PricingModuleInline(admin.TabularInline):
    model = PricingModule
    extra = 1


@admin.register(PricingCategory)
class PricingCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    inlines = [PricingModuleInline]


@admin.register(PricingModule)
class PricingModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_default', 'is_required', 'is_active', 'order')
    list_editable = ('price', 'is_default', 'is_required', 'is_active', 'order')
    list_filter = ('category', 'is_active', 'is_default', 'is_required')
    search_fields = ('name',)


@admin.register(PricingPreset)
class PricingPresetAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('modules',)
