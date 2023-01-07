# Generated by Django 4.1.1 on 2022-12-30 11:47

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0105_alter_housemodel_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='housemodel',
            name='youtube_video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]