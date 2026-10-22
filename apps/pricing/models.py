"""
Pricing models: Categories, modules, and presets for the pricing calculator.
"""
from django.db import models


class PricingCategory(models.Model):
    """Category grouping for pricing modules (e.g., Infrastructure, Design, Content)."""
    name = models.CharField('نام دسته', max_length=100)
    icon = models.CharField('آیکون', max_length=100, blank=True)
    order = models.PositiveIntegerField('ترتیب', default=0)

    class Meta:
        verbose_name = 'دسته قیمت‌گذاری'
        verbose_name_plural = 'دسته‌های قیمت‌گذاری'
        ordering = ['order']

    def __str__(self):
        return self.name


class PricingModule(models.Model):
    """Individual pricing modules that can be selected in the calculator."""
    category = models.ForeignKey(
        PricingCategory,
        on_delete=models.CASCADE,
        related_name='modules',
        verbose_name='دسته',
    )
    name = models.CharField('نام ماژول', max_length=200)
    description = models.TextField('توضیحات', blank=True)
    price = models.DecimalField('قیمت (تومان)', max_digits=12, decimal_places=0)
    is_default = models.BooleanField('پیش‌فرض فعال', default=False,
                                      help_text='آیا این ماژول به صورت پیش‌فرض انتخاب شود؟')
    is_required = models.BooleanField('الزامی', default=False,
                                       help_text='آیا این ماژول غیرقابل حذف است؟')
    order = models.PositiveIntegerField('ترتیب', default=0)
    is_active = models.BooleanField('فعال', default=True)

    class Meta:
        verbose_name = 'ماژول قیمت‌گذاری'
        verbose_name_plural = 'ماژول‌های قیمت‌گذاری'
        ordering = ['category__order', 'order']

    def __str__(self):
        return f'{self.name} - {self.price:,.0f} تومان'


class PricingPreset(models.Model):
    """Pre-configured pricing packages (e.g., Basic, Professional, Enterprise)."""
    name = models.CharField('نام بسته', max_length=200)
    slug = models.SlugField('اسلاگ', max_length=200, unique=True, allow_unicode=True)
    description = models.TextField('توضیحات', blank=True)
    modules = models.ManyToManyField(
        PricingModule,
        related_name='presets',
        verbose_name='ماژول‌ها',
    )
    is_featured = models.BooleanField('ویژه', default=False)
    order = models.PositiveIntegerField('ترتیب', default=0)
    is_active = models.BooleanField('فعال', default=True)

    class Meta:
        verbose_name = 'بسته قیمت‌گذاری'
        verbose_name_plural = 'بسته‌های قیمت‌گذاری'
        ordering = ['order']

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return self.modules.aggregate(total=models.Sum('price'))['total'] or 0
