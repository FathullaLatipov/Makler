# Generated by Django 4.1.1 on 2022-10-22 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_storemodel_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storemodel',
            name='product_status',
            field=models.CharField(choices=[('InProgress', 'InProgress'), ('PUBLISH', 'PUBLISH'), ('DELETED', 'DELETED'), ('ARCHIVED', 'ARCHIVED'), ('REJECTED', 'REJECTED')], default=('InProgress', 'InProgress'), max_length=30, null=True),
        ),
    ]
