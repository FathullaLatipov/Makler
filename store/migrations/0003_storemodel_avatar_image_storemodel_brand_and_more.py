# Generated by Django 4.1.1 on 2022-10-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_storemodel_isbookmarked'),
    ]

    operations = [
        migrations.AddField(
            model_name='storemodel',
            name='avatar_image',
            field=models.FileField(null=True, upload_to='avatar_image', verbose_name='avatar_image'),
        ),
        migrations.AddField(
            model_name='storemodel',
            name='brand',
            field=models.CharField(max_length=200, null=True, verbose_name='brand'),
        ),
        migrations.AddField(
            model_name='storemodel',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='storemodel',
            name='use_for',
            field=models.CharField(max_length=400, null=True, verbose_name='use_for'),
        ),
    ]
