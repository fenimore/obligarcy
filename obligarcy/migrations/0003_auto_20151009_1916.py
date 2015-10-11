# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0002_auto_20151008_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contracts',
        ),
        migrations.AddField(
            model_name='contract',
            name='user',
            field=models.ForeignKey(to='obligarcy.User', default=1),
        ),
    ]
