# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0017_auto_20151015_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='body',
        ),
    ]
