# Generated by Django 4.1.1 on 2022-11-02 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0046_alter_houseimagemodel_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='houses', to=settings.AUTH_USER_MODEL),
        ),
    ]
