# Generated by Django 4.1.1 on 2022-10-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0005_alter_mastermodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastermodel',
            name='isBookmarked',
            field=models.BooleanField(default=False, verbose_name='isBookmarked'),
        ),
    ]