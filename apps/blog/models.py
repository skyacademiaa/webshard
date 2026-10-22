"""
Blog models: Articles with categories, tags, and SEO.
"""
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit


class ArticleCategory(models.Model):
    """Blog article categories."""
    name = models.CharField('نام دسته‌بندی', max_length=100)
    slug = models.SlugField('اسلاگ', max_length=100, unique=True, allow_unicode=True)
    description = models.TextField('توضیحات', blank=True)
    order = models.PositiveIntegerField('ترتیب', default=0)

    class Meta:
        verbose_name = 'دسته‌بندی مقاله'
        verbose_name_plural = 'دسته‌بندی‌های مقالات'
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})


class Article(models.Model):
    """Blog article."""
    title = models.CharField('عنوان', max_length=300)
    slug = models.SlugField('اسلاگ', max_length=300, unique=True, allow_unicode=True)
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='articles',
        verbose_name='دسته‌بندی',
    )
    excerpt = models.TextField('چکیده', max_length=500, blank=True,
                                help_text='خلاصه مقاله برای نمایش در لیست')
    content = models.TextField('محتوا')
    cover = ProcessedImageField(
        verbose_name='تصویر شاخص',
        upload_to='articles/',
        processors=[ResizeToFill(800, 450)],
        format='WEBP',
        options={'quality': 85},
        blank=True,
        null=True,
    )
    tags = TaggableManager(verbose_name='تگ‌ها', blank=True)

    # Author
    author_name = models.CharField('نام نویسنده', max_length=200, blank=True)

    # Status
    is_published = models.BooleanField('منتشر شده', default=False)
    published_at = models.DateTimeField('تاریخ انتشار', blank=True, null=True)
    created_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField('تاریخ بروزرسانی', auto_now=True)

    # Stats
    views = models.PositiveIntegerField('تعداد بازدید', default=0)

    # Reading time (auto-calculated)
    reading_time = models.PositiveIntegerField('زمان مطالعه (دقیقه)', default=0)

    # SEO
    meta_title = models.CharField('عنوان متا', max_length=70, blank=True)
    meta_description = models.CharField('توضیحات متا', max_length=160, blank=True)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # Auto-set published_at
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()

        # Calculate reading time (~200 words per minute for Persian)
        if self.content:
            word_count = len(self.content.split())
            self.reading_time = max(1, word_count // 200)

        super().save(*args, **kwargs)

    def increment_views(self):
        """Increment the view count."""
        self.views += 1
        self.save(update_fields=['views'])
