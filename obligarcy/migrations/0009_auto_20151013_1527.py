# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0008_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='deadline_has_past',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract',
            name='deadline_list',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='contract',
            name='frequency',
            field=models.CharField(choices=[('O', 'Once off'), ('D', 'Daily'), ('2D', 'Every other day'), ('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')], default='O', max_length=1),
        ),
    ]
