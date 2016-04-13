# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('obligarcy', '0039_auto_20160406_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('verb', models.CharField(max_length=255)),
                ('target_id', models.PositiveIntegerField(blank=True, null=True, db_index=True)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('actor', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='actions')),
                ('target_ct', models.ForeignKey(to='contenttypes.ContentType', related_name='target_obj', blank=True, null=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
