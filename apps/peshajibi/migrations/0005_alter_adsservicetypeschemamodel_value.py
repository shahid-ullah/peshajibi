# Generated by Django 4.1.5 on 2023-03-02 06:17

import apps.peshajibi.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peshajibi', '0004_adsservicetypeschemamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsservicetypeschemamodel',
            name='value',
            field=models.JSONField(blank=True, default=apps.peshajibi.models.EMPTY_DICTIONARY),
        ),
    ]