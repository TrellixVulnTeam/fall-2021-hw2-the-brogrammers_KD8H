# Generated by Django 2.2.23 on 2021-09-26 04:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20210925_2250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewform',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.AlterField(
            model_name='reviewform',
            name='essay',
            field=models.PositiveSmallIntegerField(help_text='Essay rating of candidate (0 - 10)', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Essay'),
        ),
        migrations.AlterField(
            model_name='reviewform',
            name='interview',
            field=models.PositiveSmallIntegerField(help_text='Interview rating of candidate (0 - 10)', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Interview'),
        ),
    ]
