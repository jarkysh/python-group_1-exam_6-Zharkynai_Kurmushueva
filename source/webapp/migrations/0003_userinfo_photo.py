# Generated by Django 2.1 on 2019-01-15 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190114_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(default='https://help.github.com/assets/images/site/invertocat.png', upload_to='', verbose_name='Фотография'),
            preserve_default=False,
        ),
    ]
