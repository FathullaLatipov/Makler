# Generated by Django 4.1.1 on 2022-11-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'Store_amenities',
                'verbose_name_plural': 'Store_amenities',
            },
        ),
        migrations.AddField(
            model_name='storemodel',
            name='store_amenitites',
            field=models.ManyToManyField(to='store.storeamenities', verbose_name='store_amenities'),
        ),
    ]