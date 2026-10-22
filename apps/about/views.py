"""
About views.
"""
from django.views.generic import TemplateView
from .models import TeamMember, CompanyStat


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamMember.objects.filter(is_active=True)
        context['stats'] = CompanyStat.objects.all()
        return context
