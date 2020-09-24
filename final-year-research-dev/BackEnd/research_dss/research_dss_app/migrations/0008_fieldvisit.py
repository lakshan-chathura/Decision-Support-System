# Generated by Django 2.2.1 on 2019-08-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_dss_app', '0007_nirmap_rgbmap'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('rgb_map', models.CharField(max_length=50)),
                ('nir_map', models.CharField(max_length=50)),
                ('ndvi_map', models.CharField(max_length=50)),
                ('tile_location', models.CharField(max_length=50)),
            ],
        ),
    ]