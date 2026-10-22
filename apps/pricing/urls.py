"""
Pricing URL configuration.
"""
from django.urls import path
from .views import PricingView

app_name = 'pricing'

urlpatterns = [
    path('', PricingView.as_view(), name='calculator'),
]
