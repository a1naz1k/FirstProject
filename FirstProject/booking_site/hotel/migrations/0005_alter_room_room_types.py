# Generated by Django 5.1.3 on 2024-12-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_hotel_hotel_address_en_hotel_hotel_address_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_types',
            field=models.CharField(choices=[('люкс', 'люкс'), ('семейный', 'семейный'), ('одноком', 'одноком'), ('двухком', 'двухком')], max_length=16),
        ),
    ]
