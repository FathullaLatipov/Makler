# Generated by Django 4.1.1 on 2022-11-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0049_alter_amenitiesmodel_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenitiesmodel',
            name='title',
            field=models.CharField(max_length=300, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='pricelistmodel',
            name='price',
            field=models.CharField(max_length=10, verbose_name='price'),
        ),
    ]
