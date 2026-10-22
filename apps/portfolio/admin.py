"""
Portfolio admin configuration.
"""
from django.contrib import admin
from .models import ProjectCategory, Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 2


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_featured', 'order', 'created_at')
    list_editable = ('is_published', 'is_featured', 'order')
    list_filter = ('category', 'is_published', 'is_featured')
    search_fields = ('title', 'description', 'client_name')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    date_hierarchy = 'created_at'

    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'slug', 'category', 'short_description', 'description'),
        }),
        ('جزئیات', {
            'fields': ('client_name', 'technologies', 'website_url', 'completed_at'),
        }),
        ('تصاویر', {
            'fields': ('thumbnail', 'cover'),
        }),
        ('تنظیمات', {
            'fields': ('is_published', 'is_featured', 'order'),
        }),
        ('سئو', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
        }),
    )
