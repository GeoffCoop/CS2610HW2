# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-22 04:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='authorsName',
            new_name='authors_name',
        ),
    ]