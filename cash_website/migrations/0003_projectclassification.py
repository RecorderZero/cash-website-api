# Generated by Django 5.0.4 on 2024-04-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_website', '0002_alter_classification_english_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_text', models.CharField(max_length=15)),
                ('english_text', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
