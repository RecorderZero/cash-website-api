# Generated by Django 5.0.4 on 2024-04-13 03:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_website', '0004_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('position', models.TextField()),
                ('office', models.TextField()),
                ('onboard_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cash_website.member'),
        ),
    ]
