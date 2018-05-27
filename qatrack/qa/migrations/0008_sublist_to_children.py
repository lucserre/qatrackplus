# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 16:02
from __future__ import unicode_literals

from django.db import migrations


def sublists_to_children(apps, schema):

    TestList = apps.get_model("qa", "TestList")
    Sublist = apps.get_model("qa", "Sublist")

    for tl in TestList.objects.filter(sublists__isnull=False):
        ntests = tl.tests.count()
        for i, sublist in enumerate(tl.sublists.order_by("name")):
            Sublist.objects.create(parent=tl, child=sublist, order=ntests + i)
            tl.sublists.remove(sublist)


def children_to_sublists(apps, schema):

    TestList = apps.get_model("qa", "TestList")

    for tl in TestList.objects.filter(children__isnull=False):
        for child in tl.sublists.all():
            tl.sublists.add(child)


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0007_auto_20171124_1102'),
    ]

    operations = [
        migrations.RunPython(sublists_to_children, children_to_sublists)
    ]
