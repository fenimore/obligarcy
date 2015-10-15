# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0019_auto_20151015_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadline',
            name='deadline',
            field=models.DateTimeField(verbose_name='deadline'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(null=True, upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(null=True),
        ),
    ]
