# Generated by Django 2.2.1 on 2019-06-30 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research_dss_app', '0005_auto_20190630_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ndvimap',
            old_name='nir_path',
            new_name='nir_map',
        ),
        migrations.RenameField(
            model_name='ndvimap',
            old_name='rgb_path',
            new_name='rgb_map',
        ),
    ]
