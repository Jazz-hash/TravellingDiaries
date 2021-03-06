# Generated by Django 2.2.5 on 2020-01-21 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_auto_20200106_2048'),
        ('reviews', '0013_auto_20200120_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='destination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='destinations.Destination'),
            preserve_default=False,
        ),
    ]
