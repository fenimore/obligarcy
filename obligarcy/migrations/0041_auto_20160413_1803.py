# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0040_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='target_id',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
