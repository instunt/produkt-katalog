# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Selekcia', '0006_produkt_cena'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='mena',
            field=models.CharField(default='EUR', max_length=3),
        ),
    ]
