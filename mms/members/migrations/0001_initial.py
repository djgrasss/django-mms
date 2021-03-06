# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('account', models.ForeignKey(to='accounting.LedgerAccount')),
            ],
        ),
        migrations.CreateModel(
            name='MembershipLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('cost', models.DecimalField(max_digits=8, decimal_places=2)),
                ('per', models.PositiveSmallIntegerField(default=1, choices=[(1, b'/month'), (3, b'/quarter'), (12, b'/year')])),
                ('has_keyfob', models.BooleanField()),
                ('has_room_key', models.BooleanField()),
                ('has_voting', models.BooleanField()),
                ('has_powertool_access', models.BooleanField()),
                ('account', models.ForeignKey(to='accounting.LedgerAccount')),
            ],
        ),
    ]
