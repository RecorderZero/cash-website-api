# Generated by Django 5.0.4 on 2024-05-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_website', '0028_carouselimage_date_carouselimage_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='employee',
            field=models.ManyToManyField(blank=True, to='cash_website.employee'),
        ),
    ]
