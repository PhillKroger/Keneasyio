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

