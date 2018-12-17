# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-17 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0028_auto_20181214_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testinstance',
            options={'get_latest_by': 'work_completed', 'permissions': (('can_view_history', 'Can see test history when performing QC'), ('can_view_charts', 'Can view charts of test history'), ('can_run_sql_reports', 'Can run SQL Data Reports'), ('can_create_sql_reports', 'Can create SQL Data Reports'), ('can_review', 'Can review & approve tests'), ('can_skip_without_comment', 'Can skip tests without comment'), ('can_review_own_tests', 'Can review & approve  self-performed tests'))},
        ),
    ]
