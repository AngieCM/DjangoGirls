# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salseando', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gruposalsa',
            name='imagen',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
