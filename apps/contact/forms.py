"""
Contact forms.
"""
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'نام و نام خانوادگی',
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
            'subject': forms.TextInput(attrs={
                'placeholder': 'موضوع پیام',
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'پیام خود را بنویسید...',
                'class': 'form-textarea',
                'rows': 5,
            }),
        }
