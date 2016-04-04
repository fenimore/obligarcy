# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0030_auto_20160403_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to='obligarcy.UserProfile'),
        ),
    ]
