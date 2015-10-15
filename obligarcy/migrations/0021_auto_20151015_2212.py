# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import obligarcy.models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0020_auto_20151015_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.CharField(unique=True, primary_key=True, default=obligarcy.models.pkgen, serialize=False, max_length=6),
        ),
    ]
