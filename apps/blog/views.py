"""
Blog views.
"""
from django.views.generic import ListView, DetailView
from .models import Article, ArticleCategory


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/list.html'
    context_object_name = 'articles'
    paginate_by = 9
    queryset = Article.objects.filter(is_published=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all()
        return context


class ArticleByCategoryView(ListView):
    model = Article
    template_name = 'blog/list.html'
    context_object_name = 'articles'
    paginate_by = 9

    def get_queryset(self):
        return Article.objects.filter(
            is_published=True,
            category__slug=self.kwargs['slug'],
        ).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all()
        context['active_category'] = self.kwargs['slug']
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'
    slug_field = 'slug'

    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.increment_views()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_articles'] = Article.objects.filter(
            is_published=True,
            category=self.object.category,
        ).exclude(pk=self.object.pk)[:3]
        return context
