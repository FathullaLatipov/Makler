# Generated by Django 4.1.1 on 2023-01-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0008_alter_mebelmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mebelmodel',
            name='long_descriptions',
            field=models.TextField(null=True, verbose_name='descriptions'),
        ),
    ]
