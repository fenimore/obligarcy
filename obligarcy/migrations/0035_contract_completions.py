# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obligarcy', '0034_auto_20160404_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='completions',
            field=models.ManyToManyField(related_name='completed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
