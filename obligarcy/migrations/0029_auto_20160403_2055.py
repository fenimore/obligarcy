# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0028_auto_20160403_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deadline',
            name='submission',
        ),
        migrations.AddField(
            model_name='deadline',
            name='submission',
            field=models.ForeignKey(to='obligarcy.Submission', default=0),
            preserve_default=False,
        ),
    ]
