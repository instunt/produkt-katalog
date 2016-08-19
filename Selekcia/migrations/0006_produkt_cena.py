# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Selekcia', '0005_remove_produkt_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='cena',
            field=models.FloatField(default=0),
        ),
    ]
