# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ind', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volin_user',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('user_id', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
                ('volin', models.ManyToManyField(to='Ind.Volin', blank=True, null=True)),
            ],
        ),
    ]
