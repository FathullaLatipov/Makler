# Generated by Django 4.1.1 on 2023-01-04 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewMebelImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(null=True, upload_to='API/mebel/images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mebel.mebelmodel')),
            ],
        ),
    ]
