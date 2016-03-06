# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-06 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id_license', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('idetificationNumber', models.CharField(max_length=13)),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('experience', models.IntegerField()),
                ('id_bus', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bus.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id_user', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('idetificationNumber', models.CharField(max_length=13)),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('user_type', models.CharField(max_length=20)),
                ('id_bus', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bus.Bus_schedule')),
            ],
        ),
    ]
