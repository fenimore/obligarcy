# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import obligarcy.models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0015_auto_20151015_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='id',
            field=models.CharField(unique=True, max_length=6, default=obligarcy.models.pkgen, primary_key=True, serialize=False),
        ),
    ]
