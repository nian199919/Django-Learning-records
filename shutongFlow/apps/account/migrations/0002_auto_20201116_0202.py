# Generated by Django 2.0.4 on 2020-11-16 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shutonguser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='允许登录admin'),
        ),
    ]
