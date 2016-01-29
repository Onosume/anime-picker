# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_title', models.TextField(blank=True)),
                ('alt_title', models.TextField(blank=True, null=True)),
                ('anime_type', models.CharField(choices=[('TV', 'TV'), ('Movie', 'Movie'), ('OVA', 'OVA'), ('ONA', 'ONA'), ('Special', 'Special')], default='TV', max_length=10)),
                ('anime_genre', models.TextField(blank=True)),
                ('current_episodes', models.IntegerField(default=0)),
                ('max_episodes', models.IntegerField(default=0)),
                ('release_season', models.CharField(max_length=15)),
                ('studio_name', models.TextField(blank=True)),
            ],
        ),
    ]
