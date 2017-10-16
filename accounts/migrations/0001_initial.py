# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-16 13:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, default='', max_length=30)),
                ('street_number', models.IntegerField(blank=True, null=True)),
                ('street_name', models.CharField(blank=True, default='', max_length=30)),
                ('suburb', models.CharField(blank=True, default='', max_length=30)),
                ('postcode', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userTypeAccessModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.CharField(default='', max_length=10)),
                ('accessableFeatures', models.CharField(default='', max_length=100000)),
            ],
        ),
    ]