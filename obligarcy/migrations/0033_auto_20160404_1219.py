# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0032_remove_userprofile_follows'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='is_expired',
            new_name='is_active',
        ),
    ]
