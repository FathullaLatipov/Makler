# Generated by Django 4.1.1 on 2022-11-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0064_housemodel_property_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='housemodel',
            name='app_new_building',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
