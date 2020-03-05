# Generated by Django 2.2.5 on 2020-03-05 21:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotels', '0002_hotelimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]