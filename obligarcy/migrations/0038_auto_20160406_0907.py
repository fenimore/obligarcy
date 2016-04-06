# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0037_userprofile_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='profile_images', null=True),
        ),
    ]
