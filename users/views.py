from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.core.mail import send_mail
from django.contrib.auth import login
from django.conf import settings
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        user.email_user(
            subject='Добро пожаловать в наш интернет-магазин!',
            message='Спасибо, что зарегистрировались в нашем сервисе!')
        return super().form_valid(form)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('users:profile_edit')  # Используем namespace

    def get_object(self, queryset=None):
        return self.request.user
