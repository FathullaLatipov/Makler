# Generated by Django 4.0 on 2022-12-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0097_alter_housemodel_object'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='object',
            field=models.CharField(blank=True, choices=[('квартиру', 'квартиру'), ('комната', 'комната'), ('дача', 'дача'), ('дома', 'дома'), ('участка', 'участка'), ('townhouse', 'Townhouse'), ('bed_space', 'Bed_space')], default=None, max_length=200, null=True),
        ),
    ]
