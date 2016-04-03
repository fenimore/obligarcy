# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0027_auto_20160403_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='deadline_has_past',
            new_name='is_expired',
        ),
        migrations.RenameField(
            model_name='deadline',
            old_name='accomplished',
            new_name='is_accomplished',
        ),
        migrations.RenameField(
            model_name='deadline',
            old_name='late_accomplished',
            new_name='is_expired',
        ),
        migrations.AddField(
            model_name='deadline',
            name='is_late',
            field=models.BooleanField(default=False),
        ),
    ]
