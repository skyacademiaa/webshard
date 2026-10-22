"""
Blog URL configuration.
"""
from django.urls import path
from .views import ArticleListView, ArticleByCategoryView, ArticleDetailView

app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('category/<slug:slug>/', ArticleByCategoryView.as_view(), name='category'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
]
