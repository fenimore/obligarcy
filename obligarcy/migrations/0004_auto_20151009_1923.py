# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0003_auto_20151009_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='user',
        ),
        migrations.AddField(
            model_name='contract',
            name='user',
            field=models.ManyToManyField(default=1, to='obligarcy.User'),
        ),
    ]
