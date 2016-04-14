# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0041_auto_20160413_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.RenameField(
            model_name='action',
            old_name='created',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='contract',
            name='title',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
