
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'thumbnail', 'body', 'pub_date')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')