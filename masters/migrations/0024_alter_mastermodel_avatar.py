# Generated by Django 4.0 on 2022-12-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0023_alter_mastermodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastermodel',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='master_avatar', verbose_name='avatar'),
        ),
    ]
