# Generated by Django 4.0 on 2022-12-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0083_userwishlistmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='web_address_longtitude',
            field=models.FloatField(null=True, verbose_name='web_address_longtitude'),
        ),
    ]