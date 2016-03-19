# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='date',
            field=models.DateField(help_text='Data (RRRR-MM-DD)'),
        ),
        migrations.AlterField(
            model_name='docs',
            name='place',
            field=models.CharField(help_text='Miejscowosc', max_length=30),
        ),
        migrations.AlterField(
            model_name='docs',
            name='sign1',
            field=models.TextField(help_text='Podpis'),
        ),
        migrations.AlterField(
            model_name='docs',
            name='text',
            field=models.TextField(help_text='Tekst'),
        ),
        migrations.AlterField(
            model_name='docs',
            name='title',
            field=models.CharField(help_text='Naglowek', max_length=60),
        ),
    ]
