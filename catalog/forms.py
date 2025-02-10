from django.forms import BooleanField, ModelForm
from django.core.exceptions import ValidationError

from catalog.models import Product, Category

forbidden_words = [
    'казино',
    'биржа',
    'обман',
    'криптовалюта',
    'дешево',
    'полиция',
    'крипта',
    'бесплатно',
    'радар'
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field, in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Введите наименование продукта' })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Введите описание продукта'
        })
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({
            'placeholder': 'Введите цену продукта'
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError(f'Использование слова "{word}" в названии продукта запрещено')
            return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in forbidden_words:
            if word in description.lower():
                raise ValidationError(f'Использование слова "{word}" в описании продукта запрещено')
            return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError(f'Цена не может быть "{price}"')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        variants = ('.jpeg', '.png', 'jpg')
        if image:
            if not image.name.lower().endswith(variants):
                raise ValidationError('Неверный формат файла')
            if image.size > 5 * 1024 * 1024:
                raise ValidationError('Размер файла превышает допустимый размер 5 MB')
        return image


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("status_publication", )


class CategoryForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description')
