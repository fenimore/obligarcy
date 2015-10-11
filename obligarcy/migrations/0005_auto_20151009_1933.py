# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obligarcy', '0004_auto_20151009_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('body', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='submitted')),
            ],
        ),
        migrations.RemoveField(
            model_name='contract',
            name='user',
        ),
        migrations.AddField(
            model_name='contract',
            name='users',
            field=models.ManyToManyField(to='obligarcy.User'),
        ),
        migrations.AddField(
            model_name='submission',
            name='contract',
            field=models.ForeignKey(to='obligarcy.Contract'),
        ),
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(to='obligarcy.User'),
        ),
    ]
