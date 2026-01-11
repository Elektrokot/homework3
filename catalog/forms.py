from django import forms
from .models import Product
from django.core.exceptions import ValidationError


BANNED_WORDS = [  # Запрещённые слова, можно легко добавлять.
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]


def validate_image(value):
    """
    Валидация изображения: формат и размер.
    """
    filesize = value.size
    allowed_extensions = ['.jpg', '.jpeg', '.png']
    ext = value.name.lower()[value.name.lower().rfind('.'):]

    if ext not in allowed_extensions:
        raise ValidationError('Файл должен быть в формате JPG или PNG.')

    if filesize > 5 * 1024 * 1024:  # 5 МБ
        raise ValidationError('Размер файла не должен превышать 5 МБ.')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара',
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену',
        })

    def clean_title(self):
        """
        Валидация поля "Наименование товара"
        :return: Title
        """
        title = self.cleaned_data.get('title')
        if title:
            for word in BANNED_WORDS:
                if word.lower() in title.lower():
                    raise forms.ValidationError(f"Поле 'Название' содержит запрещённое слово: '{word}'.")
        return title

    def clean_description(self):
        """
        Валидация поля "Описание"
        :return: Description
        """
        description = self.cleaned_data.get('description')
        if description:
            for word in BANNED_WORDS:
                if word.lower() in description.lower():
                    raise forms.ValidationError(f"Поле 'Описание' содержит запрещённое слово: '{word}'.")
        return description

    def clean_price(self):
        """
        Валидация цены.
        :return: Price
        """
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Цена не может быть отрицательной или нулевой.")
        return price

    def clean_image(self):
        """
        Валидация изображения
        :return: Image
        """
        image = self.cleaned_data.get('image')
        if image:
            validate_image(image)
        return image