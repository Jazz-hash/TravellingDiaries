# Generated by Django 2.2.5 on 2020-03-05 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('T', 'Train'), ('B', 'Bus'), ('P', 'Plane')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='transport-images')),
                ('transport', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='transport_images', to='transport.Transport')),
            ],
        ),
    ]
