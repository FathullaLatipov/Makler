# Generated by Django 4.1.1 on 2022-10-06 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_remove_mastermodel_activity_and_more'),
        ('masters', '0003_alter_mastermodel_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastermodel',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='products.mapmodel', verbose_name='address'),
        ),
    ]
