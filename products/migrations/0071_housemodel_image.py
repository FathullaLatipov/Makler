# Generated by Django 4.1.2 on 2022-12-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0070_housemodel_web_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='housemodel',
            name='image',
            field=models.ImageField(null=True, upload_to='Product/APi'),
        ),
    ]
