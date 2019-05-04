# Generated by Django 2.1.3 on 2018-12-19 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Citybus1', '0004_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sea', models.PositiveIntegerField()),
                ('ocu', models.BooleanField()),
                ('hol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Citybus1.User')),
                ('sch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Citybus1.Schedule')),
            ],
        ),
    ]
