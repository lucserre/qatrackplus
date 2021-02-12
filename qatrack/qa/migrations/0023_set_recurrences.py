# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-19 17:44
from __future__ import unicode_literals

from django.db import migrations
from django.utils import timezone
import recurrence

from qatrack.qatrack_core.scheduling import calc_nominal_interval


def create_freq_schedule(apps, schema):

    Frequency = apps.get_model("qa", "Frequency")
    from_ = timezone.datetime(2012, 1, 1, tzinfo=timezone.get_current_timezone())

    for f in Frequency.objects.all():
        rule = recurrence.Rule(recurrence.DAILY, interval=f.due_interval)
        f.recurrences = recurrence.Recurrence(rrules=[rule], dtstart=from_)
        f.overdue_interval = max(1, f.overdue_interval - f.nominal_interval)
        f.nominal_interval = calc_nominal_interval(f)
        f.save()


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0022_auto_20181120_1607'),
    ]

    operations = [migrations.RunPython(create_freq_schedule, reverse_code=lambda a, s: None)]
