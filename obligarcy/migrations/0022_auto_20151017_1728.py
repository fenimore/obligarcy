# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0021_auto_20151015_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deadline',
            name='submission',
        ),
        migrations.AddField(
            model_name='deadline',
            name='submission',
            field=models.ManyToManyField(to='obligarcy.Submission', null=True),
        ),
    ]
