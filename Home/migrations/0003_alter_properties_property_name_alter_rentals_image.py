# Generated by Django 5.0.3 on 2024-03-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_remove_rentals_user_properties_property_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='property_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='rentals',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name=''),
        ),
    ]
