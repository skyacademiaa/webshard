"""
Services models.
"""
from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit


class Service(models.Model):
    """A service offered by the company (e.g., Web Design, CRM, CMS)."""
    title = models.CharField('عنوان خدمت', max_length=200)
    slug = models.SlugField('اسلاگ', max_length=200, unique=True, allow_unicode=True)
    short_description = models.CharField('توضیح کوتاه', max_length=300)
    description = models.TextField('توضیحات کامل')
    icon = models.CharField(
        'آیکون',
        max_length=100,
        help_text='نام آیکون SVG (مثال: globe-alt)',
        blank=True,
    )
    cover = ProcessedImageField(
        verbose_name='تصویر کاور',
        upload_to='services/',
        processors=[ResizeToFill(800, 500)],
        format='WEBP',
        options={'quality': 85},
        blank=True,
        null=True,
    )
    order = models.PositiveIntegerField('ترتیب', default=0)
    is_active = models.BooleanField('فعال', default=True)
    created_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField('تاریخ بروزرسانی', auto_now=True)

    # SEO
    meta_title = models.CharField('عنوان متا', max_length=70, blank=True)
    meta_description = models.CharField('توضیحات متا', max_length=160, blank=True)

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})


class ServiceFeature(models.Model):
    """Features/capabilities for a service."""
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='features',
        verbose_name='خدمت',
    )
    title = models.CharField('عنوان ویژگی', max_length=200)
    description = models.TextField('توضیحات', blank=True)
    icon = models.CharField('آیکون', max_length=100, blank=True)
    order = models.PositiveIntegerField('ترتیب', default=0)

    class Meta:
        verbose_name = 'ویژگی خدمت'
        verbose_name_plural = 'ویژگی‌های خدمات'
        ordering = ['order']

    def __str__(self):
        return f'{self.service.title} - {self.title}'
