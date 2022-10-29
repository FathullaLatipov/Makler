# Generated by Django 4.1.1 on 2022-10-29 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='store_images', verbose_name='image')),
                ('brand_image', models.FileField(null=True, upload_to='avatar_image', verbose_name='brand_image')),
                ('brand', models.CharField(max_length=200, null=True, verbose_name='brand')),
                ('price', models.PositiveIntegerField(null=True, verbose_name='price')),
                ('use_for', models.CharField(max_length=400, null=True, verbose_name='use_for')),
                ('phoneNumber', models.PositiveIntegerField(verbose_name='phoneNumber')),
                ('address', models.CharField(max_length=400, null=True, verbose_name='address')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('isBookmarked', models.BooleanField(default=False, verbose_name='isBookmarked')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('draft', models.BooleanField(default=False)),
                ('product_status', models.CharField(choices=[('InProgress', 'InProgress'), ('PUBLISH', 'PUBLISH'), ('DELETED', 'DELETED'), ('ARCHIVED', 'ARCHIVED'), ('REJECTED', 'REJECTED')], default=('InProgress', 'InProgress'), max_length=30, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Обустройствo дома',
                'verbose_name_plural': 'Обустройствo дома',
                'ordering': ['-id'],
            },
        ),
    ]
