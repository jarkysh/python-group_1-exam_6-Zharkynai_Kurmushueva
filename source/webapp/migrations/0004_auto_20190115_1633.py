# Generated by Django 2.1 on 2019-01-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_userinfo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]
