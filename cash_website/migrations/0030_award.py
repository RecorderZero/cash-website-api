# Generated by Django 5.0.4 on 2024-05-08 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_website', '0029_alter_project_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
