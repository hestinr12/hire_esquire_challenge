# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_keeper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeentry',
            old_name='time_stamp',
            new_name='date_stamp',
        ),
        migrations.AlterField(
            model_name='job',
            name='total_minutes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
