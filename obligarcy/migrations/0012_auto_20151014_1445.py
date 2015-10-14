# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0011_auto_20151014_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('deadline', models.DateTimeField(verbose_name='deadline')),
            ],
        ),
        migrations.AlterField(
            model_name='contract',
            name='deadline_list',
            field=models.CharField(max_length=3000, default=''),
        ),
        migrations.AddField(
            model_name='deadline',
            name='contract',
            field=models.ForeignKey(to='obligarcy.Contract'),
        ),
    ]
