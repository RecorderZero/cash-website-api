# Generated by Django 5.0.4 on 2024-05-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_website', '0031_new_subtitle_project_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=10)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='employee',
        ),
    ]
