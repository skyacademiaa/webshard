"""
Context processor to make site settings available in all templates.
"""
from .models import SiteSettings


def site_settings(request):
    """Add site settings to template context."""
    try:
        settings = SiteSettings.load()
    except Exception:
        settings = None
    return {'site_settings': settings}
