# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0016_auto_20151015_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='conditions',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='penalties',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='preamble',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
