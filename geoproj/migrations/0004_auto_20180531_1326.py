# Generated by Django 2.0.5 on 2018-05-31 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoproj', '0003_auto_20180531_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dem',
            name='data_source1',
        ),
        migrations.DeleteModel(
            name='DEM',
        ),
    ]
