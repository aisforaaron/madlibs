# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('story_title', models.CharField(max_length=255)),
                ('story_body', models.TextField(help_text=b'Enter your story and use {token} as values you want to replace. Use dashes instead of spaces. For example, {noun}, {plural-noun} and {verb}.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
