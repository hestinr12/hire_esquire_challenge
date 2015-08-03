# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('total_minutes', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('minutes_worked', models.PositiveSmallIntegerField()),
                ('time_stamp', models.DateField()),
                ('work_summary', models.CharField(max_length=300)),
                ('related_job', models.ForeignKey(to='time_keeper.Job')),
            ],
        ),
    ]
