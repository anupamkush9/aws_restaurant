# Generated by Django 3.2.7 on 2021-09-24 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_image',
            field=models.ImageField(blank=True, upload_to='hotel_image'),
        ),
    ]
