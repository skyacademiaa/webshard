"""
Services views.
"""
from django.views.generic import ListView, DetailView
from .models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'services/list.html'
    context_object_name = 'services'
    queryset = Service.objects.filter(is_active=True).prefetch_related('features')


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/detail.html'
    context_object_name = 'service'
    slug_field = 'slug'

    def get_queryset(self):
        return Service.objects.filter(is_active=True).prefetch_related('features')
