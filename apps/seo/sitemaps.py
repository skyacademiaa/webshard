"""
Django sitemaps for SEO.
"""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.services.models import Service
from apps.portfolio.models import Project
from apps.blog.models import Article


class StaticViewSitemap(Sitemap):
    """Sitemap for static pages."""
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['core:home', 'services:list', 'portfolio:list',
                'pricing:calculator', 'blog:list', 'about:about',
                'contact:contact', 'quote:quote']

    def location(self, item):
        return reverse(item)


class ServiceSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Service.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Project.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.created_at


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Article.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


sitemaps_dict = {
    'static': StaticViewSitemap,
    'services': ServiceSitemap,
    'projects': ProjectSitemap,
    'articles': ArticleSitemap,
}
