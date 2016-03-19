# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messege', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(verbose_name='Tresc Wiadomosci'),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(verbose_name='Temat Wiadomosci ', max_length=50),
        ),
    ]
