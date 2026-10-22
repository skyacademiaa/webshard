"""
Quote forms.
"""
from django import forms
from .models import ProjectQuote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = ProjectQuote
        fields = ['name', 'company', 'phone', 'email', 'project_type',
                  'budget_range', 'timeline', 'description', 'reference_url']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'نام و نام خانوادگی',
                'class': 'form-input',
            }),
            'company': forms.TextInput(attrs={
                'placeholder': 'نام شرکت یا سازمان (اختیاری)',
                'class': 'form-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '۰۹۱۲۳۴۵۶۷۸۹',
                'class': 'form-input',
                'dir': 'ltr',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email@example.com',
                'class': 'form-input',
                'dir': 'ltr',
            }),
            'project_type': forms.Select(attrs={
                'class': 'form-select',
            }),
            'budget_range': forms.Select(attrs={
                'class': 'form-select',
            }),
            'timeline': forms.Select(attrs={
                'class': 'form-select',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'توضیحات پروژه خود را بنویسید...',
                'class': 'form-textarea',
                'rows': 5,
            }),
            'reference_url': forms.URLInput(attrs={
                'placeholder': 'https://example.com',
                'class': 'form-input',
                'dir': 'ltr',
            }),
        }
