# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0023_auto_20151017_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=144, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
