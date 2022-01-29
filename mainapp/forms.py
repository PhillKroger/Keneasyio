from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(label='title', widget=forms.TextInput(attrs={'class': 'post_form_title', 'id': 'post_form_title_label'}))
    text = forms.CharField(label='text', widget=CKEditorWidget(attrs={'class': 'post_form_text', 'id': 'post_form_text_label'}))

    class Meta:
        model = Post
        fields = ('title', 'text')
