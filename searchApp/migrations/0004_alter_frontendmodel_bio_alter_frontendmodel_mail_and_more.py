# Generated by Django 4.0 on 2021-12-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0003_frontendmodel_avatar_url_fullstackmodel_avatar_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontendmodel',
            name='bio',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='frontendmodel',
            name='mail',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='frontendmodel',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fullstackmodel',
            name='bio',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='fullstackmodel',
            name='mail',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fullstackmodel',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mobiledevmodel',
            name='bio',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='mobiledevmodel',
            name='mail',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mobiledevmodel',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
