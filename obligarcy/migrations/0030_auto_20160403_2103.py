# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0029_auto_20160403_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadline',
            name='submission',
            field=models.ForeignKey(null=True, to='obligarcy.Submission'),
        ),
    ]
