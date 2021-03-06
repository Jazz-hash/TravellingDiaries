# Generated by Django 2.2.5 on 2020-03-05 21:19

from django.conf import settings
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotel_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='hotel_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
