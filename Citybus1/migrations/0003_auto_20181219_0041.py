# Generated by Django 2.1.3 on 2018-12-18 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citybus1', '0002_bus_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='path',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='path',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
