from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost

# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(published=True)

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj

class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'published']
    template_name = 'form.html'
    success_url = reverse_lazy('blog:blog_list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'published']
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.pk})

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
