# Generated by Django 4.1.3 on 2023-05-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_place_place_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_pic',
            field=models.ImageField(upload_to='images/', verbose_name='Фотка'),
        ),
    ]