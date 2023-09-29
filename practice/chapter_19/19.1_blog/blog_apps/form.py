from dataclasses import field
from django import forms

from .models import Blog, Article

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']
        labels = {'name': ''}

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['topic','text']
        labels = {'topic': 'topic', 'text': 'text'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80})
        }
