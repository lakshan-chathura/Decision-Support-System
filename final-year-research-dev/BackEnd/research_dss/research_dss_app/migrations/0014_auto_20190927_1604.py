# Generated by Django 2.2.1 on 2019-09-27 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research_dss_app', '0013_auto_20190822_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planthealth',
            name='ndvi_map',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='research_dss_app.FieldVisit'),
        ),
    ]
