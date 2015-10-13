# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0009_auto_20151013_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='frequency',
            field=models.CharField(max_length=2, default='O'),
        ),
    ]
