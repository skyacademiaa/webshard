"""
Blog admin configuration.
"""
from django.contrib import admin
from .models import ArticleCategory, Article


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'views', 'reading_time', 'published_at')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'created_at')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    readonly_fields = ('views', 'reading_time', 'created_at', 'updated_at')

    fieldsets = (
        ('محتوا', {
            'fields': ('title', 'slug', 'category', 'excerpt', 'content', 'cover', 'tags'),
        }),
        ('نویسنده', {
            'fields': ('author_name',),
        }),
        ('وضعیت', {
            'fields': ('is_published', 'published_at'),
        }),
        ('آمار', {
            'fields': ('views', 'reading_time', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
        ('سئو', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
        }),
    )
