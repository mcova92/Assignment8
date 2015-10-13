# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term_code', models.IntegerField(default=0)),
                ('term_Description', models.CharField(max_length=200)),
                ('crn', models.IntegerField(default=0)),
                ('subj', models.CharField(max_length=200)),
            ],
        ),
    ]
