# Generated by Django 4.1.1 on 2023-01-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0028_mastermodel_youtube_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastermodel',
            name='youtube_video',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
