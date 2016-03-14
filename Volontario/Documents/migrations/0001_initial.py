# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_place', models.CharField(max_length=40)),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=30)),
                ('dest_to', models.TextField()),
                ('title', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('sign1', models.TextField()),
                ('sign2', models.TextField()),
                ('header', models.TextField()),
            ],
        ),
    ]
