# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0010_auto_20151013_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='deadline_list',
            field=picklefield.fields.PickledObjectField(editable=False),
        ),
    ]
