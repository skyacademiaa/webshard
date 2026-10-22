"""
Core models: Site settings, sliders, and testimonials.
These are shared across the entire site.
"""
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit


class SingletonModel(models.Model):
    """Abstract base class for singleton models (like SiteSettings)."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # Prevent deletion

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(SingletonModel):
    """Global site settings - only one instance allowed."""
    site_name = models.CharField('نام سایت', max_length=200, default='Tech Service')
    tagline = models.CharField('شعار سایت', max_length=300, blank=True)
    description = models.TextField('توضیحات سایت', blank=True)

    # Logo
    logo = models.ImageField('لوگو', upload_to='site/', blank=True)
    logo_dark = models.ImageField('لوگو (حالت تیره)', upload_to='site/', blank=True)
    favicon = models.ImageField('آیکون سایت', upload_to='site/', blank=True)

    # Contact info
    phone_1 = models.CharField('شماره تماس ۱', max_length=20, blank=True)
    phone_2 = models.CharField('شماره تماس ۲', max_length=20, blank=True)
    email = models.EmailField('ایمیل', blank=True)
    address = models.TextField('آدرس', blank=True)
    working_hours = models.CharField('ساعات کاری', max_length=200, blank=True)

    # Social links
    instagram = models.URLField('اینستاگرام', blank=True)
    telegram = models.URLField('تلگرام', blank=True)
    whatsapp = models.CharField('واتساپ', max_length=20, blank=True)
    linkedin = models.URLField('لینکدین', blank=True)
    twitter = models.URLField('توییتر', blank=True)
    github = models.URLField('گیت‌هاب', blank=True)

    # SEO
    meta_title = models.CharField('عنوان متا', max_length=70, blank=True)
    meta_description = models.CharField('توضیحات متا', max_length=160, blank=True)
    meta_keywords = models.CharField('کلمات کلیدی', max_length=300, blank=True)
    og_image = models.ImageField('تصویر اشتراک‌گذاری', upload_to='site/', blank=True)

    # Analytics
    google_analytics_id = models.CharField('Google Analytics ID', max_length=50, blank=True)

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.site_name


class Slider(models.Model):
    """Homepage hero slider."""
    title = models.CharField('عنوان', max_length=200)
    subtitle = models.CharField('زیرعنوان', max_length=300, blank=True)
    description = models.TextField('توضیحات', blank=True)
    background = ProcessedImageField(
        verbose_name='تصویر پس‌زمینه',
        upload_to='sliders/',
        processors=[ResizeToFill(1920, 900)],
        format='WEBP',
        options={'quality': 85},
    )
    cta_text = models.CharField('متن دکمه', max_length=100, blank=True, default='بیشتر بدانید')
    cta_link = models.CharField('لینک دکمه', max_length=300, blank=True, default='#')
    order = models.PositiveIntegerField('ترتیب', default=0)
    is_active = models.BooleanField('فعال', default=True)
    created_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)

    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدر'
        ordering = ['order']

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Customer testimonials/reviews."""
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    name = models.CharField('نام مشتری', max_length=200)
    company = models.CharField('شرکت', max_length=200, blank=True)
    role = models.CharField('سمت', max_length=200, blank=True)
    content = models.TextField('نظر مشتری')
    avatar = ProcessedImageField(
        verbose_name='تصویر',
        upload_to='testimonials/',
        processors=[ResizeToFill(150, 150)],
        format='WEBP',
        options={'quality': 80},
        blank=True,
        null=True,
    )
    rating = models.PositiveSmallIntegerField('امتیاز', choices=RATING_CHOICES, default=5)
    is_active = models.BooleanField('فعال', default=True)
    order = models.PositiveIntegerField('ترتیب', default=0)
    created_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)

    class Meta:
        verbose_name = 'نظر مشتری'
        verbose_name_plural = 'نظرات مشتریان'
        ordering = ['order']

    def __str__(self):
        return f'{self.name} - {self.company}'


class WorkProcess(models.Model):
    """Work process steps shown on homepage."""
    title = models.CharField('عنوان مرحله', max_length=200)
    description = models.TextField('توضیحات')
    icon = models.CharField(
        'آیکون',
        max_length=100,
        help_text='نام آیکون از Heroicons (مثال: clipboard-document-list)',
        blank=True,
    )
    order = models.PositiveIntegerField('ترتیب', default=0)
    is_active = models.BooleanField('فعال', default=True)

    class Meta:
        verbose_name = 'مرحله فرآیند'
        verbose_name_plural = 'فرآیند کاری'
        ordering = ['order']

    def __str__(self):
        return self.title
