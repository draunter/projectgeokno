# Generated by Django 2.0.5 on 2018-05-31 07:59

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geoproj', '0004_auto_20180531_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='DEM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverage', models.FloatField()),
                ('date_of_capture', models.DateField(auto_now=True)),
                ('grid_size', models.FloatField()),
                ('vertical_Accuracy', models.CharField(max_length=250)),
                ('map_projection', models.CharField(max_length=250)),
                ('horizontal_datum', models.CharField(max_length=250)),
                ('vertical_datum', models.CharField(max_length=250)),
                ('file_Format', models.CharField(max_length=250)),
                ('kml_file', models.FileField(upload_to='')),
                ('poly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('data_source1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='geoproj.Air_Lidar')),
            ],
        ),
        migrations.CreateModel(
            name='Intensity_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverage', models.FloatField()),
                ('date_of_capture', models.DateField(auto_now=True)),
                ('pixel_size', models.FloatField()),
                ('file_Format', models.CharField(max_length=250)),
                ('radiometric_resolution', models.CharField(max_length=250)),
                ('method_of_interpolation', models.CharField(max_length=250)),
                ('data_source1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='geoproj.Air_Lidar')),
            ],
        ),
    ]