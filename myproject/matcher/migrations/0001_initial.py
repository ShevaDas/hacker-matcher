# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hacker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')])),
                ('email', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('skill', models.CharField(default=b'DS', max_length=2, choices=[(b'DS', b'Designer'), (b'DV', b'Developer'), (b'OT', b'Other')])),
                ('looking_for', models.CharField(default=b'DV', max_length=2, choices=[(b'DS', b'Designer'), (b'DV', b'Developer'), (b'OT', b'Other')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
