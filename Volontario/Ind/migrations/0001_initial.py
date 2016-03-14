# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='auth.user')),
                ('title', models.CharField(max_length=100, verbose_name='Nazwa zadania')),
                ('destination', models.CharField(blank=True, max_length=50, verbose_name='Miejsce ')),
                ('description', models.TextField(verbose_name='Opis')),
                ('publication_date', models.DateTimeField(blank=True, null=True, verbose_name='Data publikacji')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
