# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0022_auto_20151017_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadline',
            name='submission',
            field=models.ManyToManyField(to='obligarcy.Submission'),
        ),
    ]
