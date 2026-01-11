from django.contrib import admin
from blog.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'published', 'views_count')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('views_count',)
    ordering = ('-created_at',)
