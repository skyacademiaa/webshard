"""
Pricing views.
"""
from django.views.generic import TemplateView
from .models import PricingCategory, PricingPreset


class PricingView(TemplateView):
    template_name = 'pricing/calculator.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PricingCategory.objects.prefetch_related(
            'modules'
        ).filter(modules__is_active=True).distinct()
        context['presets'] = PricingPreset.objects.filter(
            is_active=True
        ).prefetch_related('modules')
        return context
