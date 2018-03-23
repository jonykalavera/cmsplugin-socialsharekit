# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_socialsharekit', '0002_auto_20171031_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialsharekitplugin',
            name='center',
            field=models.BooleanField(default=True, verbose_name='center'),
        ),
    ]
