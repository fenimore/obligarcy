# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0033_auto_20160404_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='penalties',
            new_name='small_print',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='preamble',
            new_name='title',
        ),
    ]
