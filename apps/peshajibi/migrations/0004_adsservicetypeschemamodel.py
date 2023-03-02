# Generated by Django 4.1.5 on 2023-03-02 06:07

import apps.peshajibi.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peshajibi', '0003_alter_adsservicesmodel_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsServiceTypeSchemaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.PositiveIntegerField(db_index=True)),
                ('key', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('value', models.JSONField(default=apps.peshajibi.models.EMPTY_DICTIONARY)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ads_service_type_schema',
                'ordering': ['id'],
            },
        ),
    ]
