# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ind', '0003_auto_20160317_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volin_user',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='volin_user',
            name='volin',
        ),
        migrations.DeleteModel(
            name='Volin_user',
        ),
    ]
