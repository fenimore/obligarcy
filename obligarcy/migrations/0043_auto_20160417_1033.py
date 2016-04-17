# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0042_auto_20160413_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='open_sign',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='licence',
            field=models.CharField(null=True, max_length=30),
        ),
    ]
