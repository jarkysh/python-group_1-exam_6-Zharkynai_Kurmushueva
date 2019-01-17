from django import forms
from webapp.models import Post, User, UserInfo


class PostSearchForm(forms.Form):
    search_string = forms.CharField(max_length=200, required=False, label='Критерий поиска')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'author']


class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['photo', 'phone']

