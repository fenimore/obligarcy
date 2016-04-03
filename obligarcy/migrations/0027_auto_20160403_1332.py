# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obligarcy', '0026_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='deadline',
            name='accomplished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deadline',
            name='late_accomplished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deadline',
            name='signee',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
