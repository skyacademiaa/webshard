"""
Quote models: Project quote/order requests.
"""
from django.db import models


class ProjectQuote(models.Model):
    """Project order/quote request from potential clients."""

    PROJECT_TYPE_CHOICES = [
        ('corporate', 'سایت شرکتی'),
        ('ecommerce', 'فروشگاهی'),
        ('personal', 'شخصی'),
        ('crm', 'سیستم CRM'),
        ('cms', 'سیستم CMS'),
        ('other', 'سایر'),
    ]

    BUDGET_CHOICES = [
        ('under_5m', 'کمتر از ۵ میلیون تومان'),
        ('5m_10m', '۵ تا ۱۰ میلیون تومان'),
        ('10m_20m', '۱۰ تا ۲۰ میلیون تومان'),
        ('20m_50m', '۲۰ تا ۵۰ میلیون تومان'),
        ('above_50m', 'بیشتر از ۵۰ میلیون تومان'),
    ]

    TIMELINE_CHOICES = [
        ('urgent', 'فوری (کمتر از ۱ هفته)'),
        ('2weeks', '۱ تا ۲ هفته'),
        ('1month', '۲ تا ۴ هفته'),
        ('2months', '۱ تا ۲ ماه'),
        ('flexible', 'زمان‌بندی انعطاف‌پذیر'),
    ]

    STATUS_CHOICES = [
        ('new', 'جدید'),
        ('reviewing', 'در حال بررسی'),
        ('quoted', 'قیمت ارسال شده'),
        ('accepted', 'تایید شده'),
        ('rejected', 'رد شده'),
        ('completed', 'تکمیل شده'),
    ]

    # Client info
    name = models.CharField('نام', max_length=200)
    company = models.CharField('نام شرکت/سازمان', max_length=200, blank=True)
    phone = models.CharField('شماره تماس', max_length=20)
    email = models.EmailField('ایمیل', blank=True)

    # Project details
    project_type = models.CharField('نوع پروژه', max_length=20, choices=PROJECT_TYPE_CHOICES)
    budget_range = models.CharField('بودجه', max_length=20, choices=BUDGET_CHOICES, blank=True)
    timeline = models.CharField('زمان‌بندی', max_length=20, choices=TIMELINE_CHOICES, blank=True)
    description = models.TextField('توضیحات پروژه')
    reference_url = models.URLField('سایت مرجع', blank=True,
                                     help_text='لینک سایتی که دوست دارید مشابه آن باشد')

    # Internal
    status = models.CharField('وضعیت', max_length=20, choices=STATUS_CHOICES, default='new')
    admin_notes = models.TextField('یادداشت مدیر', blank=True)
    created_at = models.DateTimeField('تاریخ ثبت', auto_now_add=True)
    updated_at = models.DateTimeField('تاریخ بروزرسانی', auto_now=True)

    class Meta:
        verbose_name = 'سفارش پروژه'
        verbose_name_plural = 'سفارش‌های پروژه'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.get_project_type_display()}'
