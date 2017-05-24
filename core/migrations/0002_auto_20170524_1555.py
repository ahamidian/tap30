# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='last_latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_longitude',
            field=models.FloatField(null=True),
        ),
    ]
