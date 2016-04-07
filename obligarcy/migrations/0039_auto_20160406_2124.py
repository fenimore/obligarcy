# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0038_auto_20160406_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='is_media',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='media',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='submissions/%Y/%m/%d', null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='body',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
