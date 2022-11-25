# Generated by Django 4.1.1 on 2022-11-15 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_remove_storemodel_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='storemodel',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stores', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]