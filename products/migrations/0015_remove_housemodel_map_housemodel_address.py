# Generated by Django 4.1.1 on 2022-09-29 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_housemodel_isbookmarked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housemodel',
            name='map',
        ),
        migrations.AddField(
            model_name='housemodel',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.mapmodel', verbose_name='address'),
        ),
    ]
