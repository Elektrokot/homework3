from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost
from .forms import BlogPostForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        user = self.request.user

        is_owner = post.owner == user  # Проверяем, является ли пользователь владельцем или контент-менеджером
        is_content_manager = user.groups.filter(name='Контент-менеджер').exists()

        context['is_owner'] = is_owner
        context['is_content_manager'] = is_content_manager
        return context

class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'form.html'
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Привязываем владельца к записи в блоге
        return super().form_valid(form)

class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Контент-менеджер').exists(): # Если пользователь в группе "Контент-менеджер", он может редактировать все
            return BlogPost.objects.all()
        return BlogPost.objects.filter(owner=user)  # Иначе — только свои

class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Контент-менеджер').exists():  # Если пользователь в группе "Контент-менеджер", он может удалять все
            return BlogPost.objects.all()
        return BlogPost.objects.filter(owner=user)  # Иначе — только свои
