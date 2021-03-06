# Generated by Django 2.1.3 on 2018-12-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citybus1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=8)),
                ('mar', models.CharField(max_length=20)),
                ('mod', models.CharField(max_length=20)),
                ('yea', models.PositiveIntegerField()),
                ('sea', models.PositiveIntegerField()),
                ('cap', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=20)),
                ('pas', models.CharField(max_length=20)),
                ('nam', models.CharField(max_length=20)),
                ('sur', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('cla', models.PositiveIntegerField()),
            ],
        ),
    ]
