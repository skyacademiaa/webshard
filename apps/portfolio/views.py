"""
Portfolio views with HTMX filtering support.
"""
from django.views.generic import ListView, DetailView
from .models import Project, ProjectCategory


class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/list.html'
    context_object_name = 'projects'
    queryset = Project.objects.filter(is_published=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()
        context['active_category'] = self.request.GET.get('category', 'all')
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        category_slug = self.request.GET.get('category')
        if category_slug and category_slug != 'all':
            qs = qs.filter(category__slug=category_slug)
        return qs

    def get_template_names(self):
        """Return partial template for HTMX requests."""
        if self.request.headers.get('HX-Request'):
            return ['portfolio/partials/project_grid.html']
        return [self.template_name]


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/detail.html'
    context_object_name = 'project'
    slug_field = 'slug'

    def get_queryset(self):
        return Project.objects.filter(is_published=True).select_related(
            'category'
        ).prefetch_related('images')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = Project.objects.filter(
            is_published=True,
            category=self.object.category,
        ).exclude(pk=self.object.pk)[:3]
        return context
