# Generated by Django 4.0 on 2022-12-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0095_houseobjectmodel_housemodel_object'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housemodel',
            name='object',
            field=models.CharField(blank=True, choices=[('flat', 'Flat'), ('room', 'Room'), ('summer_cottage', 'Summer_cottage'), ('house', 'House'), ('part_house', 'Part_house'), ('townhouse', 'Townhouse'), ('bed_space', 'Bed_space')], default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='housemodel',
            name='rental_type',
            field=models.CharField(blank=True, choices=[('long_time', 'Long_time'), ('several_months', 'Several_months'), ('daily', 'Daily')], default=('several_months', 'Several_months'), max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='housemodel',
            name='type',
            field=models.CharField(blank=True, choices=[('rent', 'Rent'), ('for_sale', 'For_sale')], default=('for_sale', 'For_sale'), max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='HouseObjectModel',
        ),
        migrations.DeleteModel(
            name='HouseRentalTypeModel',
        ),
        migrations.DeleteModel(
            name='HouseTypeModel',
        ),
    ]