# Generated by Django 5.0.4 on 2024-05-24 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_website', '0036_remove_chosenaward_imageurl_chosenaward_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='可讀可新增可修改可刪除', max_length=15),
        ),
    ]
