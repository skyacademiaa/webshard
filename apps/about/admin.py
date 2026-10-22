"""
About admin configuration.
"""
from django.contrib import admin
from .models import TeamMember, CompanyStat


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'experience_years', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name', 'role')


@admin.register(CompanyStat)
class CompanyStatAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'order')
    list_editable = ('value', 'order')
