"""
About models: Team members and company statistics.
"""
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class TeamMember(models.Model):
    """Team member profile."""
    name = models.CharField('نام', max_length=200)
    role = models.CharField('سمت', max_length=200)
    bio = models.TextField('بیوگرافی', blank=True)
    photo = ProcessedImageField(
        verbose_name='تصویر',
        upload_to='team/',
        processors=[ResizeToFill(400, 400)],
        format='WEBP',
        options={'quality': 85},
        blank=True,
        null=True,
    )
    experience_years = models.PositiveIntegerField('سال‌های تجربه', default=0)

    # Social links
    linkedin = models.URLField('لینکدین', blank=True)
    github = models.URLField('گیت‌هاب', blank=True)
    telegram = models.URLField('تلگرام', blank=True)

    order = models.PositiveIntegerField('ترتیب', default=0)
    is_active = models.BooleanField('فعال', default=True)

    class Meta:
        verbose_name = 'عضو تیم'
        verbose_name_plural = 'اعضای تیم'
        ordering = ['order']

    def __str__(self):
        return f'{self.name} - {self.role}'


class CompanyStat(models.Model):
    """Company statistics shown on the about page (e.g., projects completed, years experience)."""
    title = models.CharField('عنوان', max_length=100)
    value = models.CharField('مقدار', max_length=50)
    icon = models.CharField('آیکون', max_length=100, blank=True)
    order = models.PositiveIntegerField('ترتیب', default=0)

    class Meta:
        verbose_name = 'آمار شرکت'
        verbose_name_plural = 'آمارهای شرکت'
        ordering = ['order']

    def __str__(self):
        return f'{self.title}: {self.value}'
