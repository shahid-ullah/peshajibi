# Generated by Django 4.1.5 on 2023-02-15 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_citycorporationuserprofilemodel_permanent_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountsmodel',
            name='is_donate_blood',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='accountsmodel',
            name='share_profile',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='accountsmodel',
            name='username_bng',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='accountsmodel',
            name='username_eng',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
