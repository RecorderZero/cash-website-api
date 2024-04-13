# Generated by Django 5.0.4 on 2024-04-13 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_website', '0005_member_project_location_project_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_text', models.CharField(max_length=15)),
                ('english_text', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='position',
        ),
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.ManyToManyField(to='cash_website.position'),
        ),
    ]
