# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0014_remove_contract_deadline_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadline',
            name='deadline',
            field=models.CharField(verbose_name='deadline', max_length=30),
        ),
    ]
