# Generated by Django 2.2.5 on 2020-01-20 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20200120_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[(0, 'Excellent'), (1, 'Good'), (2, 'Average'), (3, 'Poor'), (4, 'Terrible')], max_length=32),
        ),
    ]
