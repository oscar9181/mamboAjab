# Generated by Django 5.0.3 on 2024-03-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_properties_property_name_alter_rentals_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentals',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]