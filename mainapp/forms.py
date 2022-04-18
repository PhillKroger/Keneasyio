from django import forms
from .models import Post, Set, Product
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Номер телефона',
                            widget=forms.TextInput(attrs={'class': 'post_form_title', 'id': 'post_form_title_label'}))
    email = forms.CharField(label='Почта',
                            widget=forms.TextInput(attrs={'class': 'post_form_email', 'id': 'post_form_email_label'}))
    text = forms.CharField(
        label='Прикрепите фотографию докумета(удостоверения) о владении магазином одежды. Фото нужно перетащить в '
              'поле ввода снизу',
        widget=CKEditorWidget(attrs={'class': 'post_form_text', 'id': 'post_form_text_label'}))

    class Meta:
        model = Post
        fields = ('title', 'email', 'text',)


class ProductForm(forms.ModelForm):
    category_season = forms.ModelChoiceField(queryset=CategorySeason.objects.all())
    category_clothes = forms.ModelChoiceField(queryset=CategoryClothes.objects.all())
    category_size = forms.ModelChoiceField(queryset=CategorySize.objects.all())
    category_price = forms.ModelChoiceField(queryset=CategoryPrice.objects.all())
    text = forms.CharField(
        label='Прикрепите фотографию докумета(удостоверения) о владении магазином одежды. Фото нужно перетащить в '
              'поле ввода снизу',
        widget=CKEditorWidget(attrs={'class': 'post_form_text', 'id': 'post_form_text_label'}))

    class Meta:
        model = Product
        fields = ('category_size', 'category_price', 'category_season', 'category_clothes', 'img',)


class SetForm(forms.ModelForm):
    # Post.objects.filter(author=user)
    product1 = forms.ModelChoiceField(queryset=Product.objects.all())
    product2 = forms.ModelChoiceField(queryset=Product.objects.all())
    product3 = forms.ModelChoiceField(queryset=Product.objects.all())
    product4 = forms.ModelChoiceField(queryset=Product.objects.all())
    product5 = forms.ModelChoiceField(queryset=Product.objects.all())
    #product5 = forms.ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = Set
        fields = ('product1', 'product2', 'product3', 'product4', 'product5', )

