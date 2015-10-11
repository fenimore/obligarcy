# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contract',
        ),
        migrations.AddField(
            model_name='user',
            name='contracts',
            field=models.ManyToManyField(to='obligarcy.Contract'),
        ),
    ]
