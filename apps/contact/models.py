"""
Contact models.
"""
from django.db import models


class ContactMessage(models.Model):
    """Contact form submission."""
    name = models.CharField('نام', max_length=200)
    phone = models.CharField('شماره تماس', max_length=20, blank=True)
    email = models.EmailField('ایمیل', blank=True)
    subject = models.CharField('موضوع', max_length=300)
    message = models.TextField('پیام')
    created_at = models.DateTimeField('تاریخ ارسال', auto_now_add=True)
    is_read = models.BooleanField('خوانده شده', default=False)

    class Meta:
        verbose_name = 'پیام تماس'
        verbose_name_plural = 'پیام‌های تماس'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.subject}'
