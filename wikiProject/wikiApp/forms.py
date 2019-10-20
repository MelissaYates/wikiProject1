from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Article, RelatedArticle


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class LogInForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        #exclude = ['author']
        fields = ['title', 'content', 'image']


class RelatedArticleForm(ModelForm):
    class Meta:
        model = RelatedArticle
        fields = ['author', 'text', 'related_image']



