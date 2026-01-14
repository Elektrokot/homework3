from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'preview', 'published']

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите заголовок',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите содержимое статьи',
            'rows': 4,
        })

        self.fields['preview'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['published'].widget.attrs.update({
            'class': 'form-check-input',  # Для checkbox
        })
