# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0013_deadline_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='deadline_list',
        ),
    ]
