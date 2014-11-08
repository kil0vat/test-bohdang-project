# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.CharField(max_length=10)),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=20)),
                ('jabber', models.CharField(max_length=20)),
                ('skype', models.CharField(max_length=20)),
                ('other_contact', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
