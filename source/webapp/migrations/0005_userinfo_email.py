# Generated by Django 2.1 on 2019-01-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20190115_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default='qwe@qe.qwe', max_length=20, verbose_name='почта'),
            preserve_default=False,
        ),
    ]
