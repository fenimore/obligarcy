# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0005_auto_20151009_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='contract',
        ),
        migrations.AddField(
            model_name='contract',
            name='submissions',
            field=models.ManyToManyField(to='obligarcy.Submission'),
        ),
    ]
