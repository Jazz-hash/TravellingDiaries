# Generated by Django 2.2.5 on 2020-03-06 20:46

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0009_auto_20200306_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]
