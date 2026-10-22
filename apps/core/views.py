"""
Core views: Homepage.
"""
from django.views.generic import TemplateView
from .models import Slider, Testimonial, WorkProcess
from apps.services.models import Service
from apps.portfolio.models import Project
from apps.blog.models import Article


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(is_active=True)
        context['services'] = Service.objects.filter(is_active=True)[:6]
        context['featured_projects'] = Project.objects.filter(
            is_published=True, is_featured=True
        )[:6]
        context['testimonials'] = Testimonial.objects.filter(is_active=True)
        context['work_processes'] = WorkProcess.objects.filter(is_active=True)
        context['latest_articles'] = Article.objects.filter(
            is_published=True
        ).select_related('category')[:3]
        return context
