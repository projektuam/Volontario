# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Nazwa wydarzenia', max_length=100)),
                ('description', models.TextField(verbose_name='Opis')),
                ('publication_date', models.DateTimeField(verbose_name='Data publikacji', null=True, blank=True)),
                ('author', models.ForeignKey(max_length=20, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publication_date'],
            },
        ),
    ]
