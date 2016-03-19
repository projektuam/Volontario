# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0002_auto_20160319_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='docs',
            name='chart',
            field=models.CharField(blank=True, null=True, max_length=20),
        ),
        migrations.AddField(
            model_name='docs',
            name='chart2',
            field=models.CharField(blank=True, null=True, max_length=20),
        ),
        migrations.AddField(
            model_name='docs',
            name='chart3',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AddField(
            model_name='docs',
            name='chart4',
            field=models.CharField(blank=True, null=True, max_length=20),
        ),
        migrations.AddField(
            model_name='docs',
            name='form_type',
            field=models.CharField(blank=True, null=True, max_length=5),
        ),
        migrations.AddField(
            model_name='docs',
            name='sign3',
            field=models.CharField(max_length=100, blank=True, null=True, choices=[('Prezes Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM', 'Prezes Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM'), ('Opiekun Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM', 'Opiekun Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM'), ('Prodziekan', 'Prodziekan'), ('Dziekan', 'Dziekan')]),
        ),
        migrations.AddField(
            model_name='docs',
            name='sign4',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AddField(
            model_name='docs',
            name='text2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='docs',
            name='text3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='docs',
            name='text4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='docs',
            name='text5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='docs',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='docs',
            name='sign1',
            field=models.CharField(max_length=100, blank=True, null=True, choices=[('Prezes Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM', 'Prezes Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM'), ('Opiekun Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM', 'Opiekun Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM'), ('Prodziekan', 'Prodziekan'), ('Dziekan', 'Dziekan')]),
        ),
        migrations.AlterField(
            model_name='docs',
            name='sign2',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='docs',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
