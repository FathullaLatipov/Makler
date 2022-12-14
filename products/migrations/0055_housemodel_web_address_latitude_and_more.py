# Generated by Django 4.1.1 on 2022-11-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0054_rename_price_pricelistmodel_price_t'),
    ]

    operations = [
        migrations.AddField(
            model_name='housemodel',
            name='web_address_latitude',
            field=models.FloatField(default=1, verbose_name='web_address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='housemodel',
            name='web_address_longtitude',
            field=models.FloatField(default=1, verbose_name='web_address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='housemodel',
            name='web_address_title',
            field=models.CharField(default=1, max_length=400, verbose_name='web_address'),
            preserve_default=False,
        ),
    ]
