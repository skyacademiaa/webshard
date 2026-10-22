"""
Portfolio models: Project categories, projects, and project images.
"""
from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit


class ProjectCategory(models.Model):
    """Project categories for filtering (e.g., Corporate, E-commerce, Personal)."""
    name = models.CharField('نام دسته‌بندی', max_length=100)
    slug = models.SlugField('اسلاگ', max_length=100, unique=True, allow_unicode=True)
    order = models.PositiveIntegerField('ترتیب', default=0)

    class Meta:
        verbose_name = 'دسته‌بندی پروژه'
        verbose_name_plural = 'دسته‌بندی‌های پروژه'
        ordering = ['order']

    def __str__(self):
        return self.name


class Project(models.Model):
    """A portfolio project."""
    title = models.CharField('عنوان پروژه', max_length=200)
    slug = models.SlugField('اسلاگ', max_length=200, unique=True, allow_unicode=True)
    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects',
        verbose_name='دسته‌بندی',
    )
    short_description = models.CharField('توضیح کوتاه', max_length=300)
    description = models.TextField('توضیحات کامل')
    client_name = models.CharField('نام مشتری', max_length=200, blank=True)
    technologies = models.CharField('تکنولوژی‌ها', max_length=500, blank=True,
                                     help_text='فناوری‌های استفاده‌شده، با کاما جدا کنید')
    website_url = models.URLField('آدرس وب‌سایت', blank=True)

    thumbnail = ProcessedImageField(
        verbose_name='تصویر شاخص',
        upload_to='projects/thumbnails/',
        processors=[ResizeToFill(600, 400)],
        format='WEBP',
        options={'quality': 85},
    )
    cover = ProcessedImageField(
        verbose_name='تصویر کاور',
        upload_to='projects/covers/',
        processors=[ResizeToFit(1200, 800)],
        format='WEBP',
        options={'quality': 85},
        blank=True,
        null=True,
    )

    is_published = models.BooleanField('منتشر شده', default=True)
    is_featured = models.BooleanField('ویژه', default=False)
    completed_at = models.DateField('تاریخ اتمام', blank=True, null=True)
    order = models.PositiveIntegerField('ترتیب', default=0)
    created_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)

    # SEO
    meta_title = models.CharField('عنوان متا', max_length=70, blank=True)
    meta_description = models.CharField('توضیحات متا', max_length=160, blank=True)

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه‌ها'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:detail', kwargs={'slug': self.slug})

    def get_tech_list(self):
        """Return technologies as a list."""
        if self.technologies:
            return [t.strip() for t in self.technologies.split(',')]
        return []


class ProjectImage(models.Model):
    """Additional images for a project."""
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='پروژه',
    )
    image = ProcessedImageField(
        verbose_name='تصویر',
        upload_to='projects/gallery/',
        processors=[ResizeToFit(1200, 800)],
        format='WEBP',
        options={'quality': 85},
    )
    caption = models.CharField('عنوان تصویر', max_length=200, blank=True)
    order = models.PositiveIntegerField('ترتیب', default=0)

    class Meta:
        verbose_name = 'تصویر پروژه'
        verbose_name_plural = 'تصاویر پروژه'
        ordering = ['order']

    def __str__(self):
        return f'{self.project.title} - تصویر {self.order}'
