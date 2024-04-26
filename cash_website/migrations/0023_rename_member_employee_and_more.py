# Generated by Django 5.0.4 on 2024-04-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_website', '0022_carouselimage_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='Employee',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='member',
            new_name='employee',
        ),
        migrations.RemoveField(
            model_name='classification',
            name='english_text',
        ),
        migrations.RemoveField(
            model_name='position',
            name='english_text',
        ),
        migrations.RemoveField(
            model_name='projectclassification',
            name='english_text',
        ),
        migrations.AlterField(
            model_name='position',
            name='chinese_text',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='imageUrl',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
