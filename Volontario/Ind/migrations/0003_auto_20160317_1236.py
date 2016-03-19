# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ind', '0002_volin_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volin_user',
            name='user_id',
        ),
        migrations.AddField(
            model_name='volin_user',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='volin_user',
            name='volin',
        ),
        migrations.AddField(
            model_name='volin_user',
            name='volin',
            field=models.ForeignKey(to='Ind.Volin', blank=True, null=True),
        ),
    ]
