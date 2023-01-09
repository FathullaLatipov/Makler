# Generated by Django 4.1.1 on 2023-01-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0011_mebelmodel_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='mebelmodel',
            name='product_status',
            field=models.IntegerField(choices=[(0, 'InProgress'), (1, 'PUBLISH'), (2, 'DELETED'), (3, 'ARCHIVED'), (4, 'REJECTED')], default=0, null=True),
        ),
        migrations.AddField(
            model_name='mebelmodel',
            name='view_count',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]