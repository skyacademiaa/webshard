"""
Quote URL configuration.
"""
from django.urls import path
from .views import QuoteView

app_name = 'quote'

urlpatterns = [
    path('', QuoteView.as_view(), name='quote'),
]
