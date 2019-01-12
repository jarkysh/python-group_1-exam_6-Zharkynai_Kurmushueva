from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя')
    password = models.CharField(max_length=200, null=False, blank=False, verbose_name='Пароль')

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info', verbose_name='Пользователь')
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя')
    password = models.CharField(max_length=200, null=False, blank=False, verbose_name='Пароль')
    phone = models.CharField(max_length=20,verbose_name="Телефон")
    friends = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Друзья')

    def __str__(self):
        return self.user, self.name

class Post(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(max_length=200, null=False, blank=False, verbose_name='Содержимое')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author_post')
    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return "%s by %s" % (self.title, self.author)