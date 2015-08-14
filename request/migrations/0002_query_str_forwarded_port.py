# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial.py'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='query_string',
            fields=models.CharField(max_length=255, verbose_name='query string', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='x_forwarded_for',
            fields=models.CharField(max_length=255, verbose_name='x_forwarded_for', blank=True),
            preserve_default=False,
        ),
    ]
