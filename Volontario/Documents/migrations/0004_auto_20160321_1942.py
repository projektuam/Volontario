# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0003_auto_20160319_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docs',
            options={'ordering': ['-id']},
        ),
    ]
