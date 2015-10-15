# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0012_auto_20151014_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='deadline',
            name='submission',
            field=models.ForeignKey(to='obligarcy.Submission', null=True),
        ),
    ]
