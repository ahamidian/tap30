# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('number', models.CharField(max_length=11)),
                ('last_latitude', models.FloatField()),
                ('last_longitude', models.FloatField()),
            ],
        ),
    ]
