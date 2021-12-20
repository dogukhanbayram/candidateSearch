# Generated by Django 4.0 on 2021-12-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0002_fullstackmodel_mobiledevmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontendmodel',
            name='avatar_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fullstackmodel',
            name='avatar_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mobiledevmodel',
            name='avatar_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]