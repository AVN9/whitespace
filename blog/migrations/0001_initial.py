# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-28 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_published', models.DateField(verbose_name='Date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('contact_no', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=250)),
                ('sex', models.CharField(max_length=5)),
                ('company', models.CharField(max_length=50)),
                ('websites', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
    ]
