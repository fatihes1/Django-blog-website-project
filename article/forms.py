from django import forms
from django.forms import fields

from .models import Article # şuanki dizindeki models doyasından article dahil edildi


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "article_image"]