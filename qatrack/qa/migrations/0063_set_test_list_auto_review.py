# Generated by Django 2.2.18 on 2021-12-24 04:56
import logging

from django.db import migrations


logger = logging.getLogger("qatrack.migrations")


def test_arrs_to_test_list_arrs(apps, schema):

    TestList = apps.get_model("qa", "TestList")
    Test = apps.get_model("qa", "Test")

    for test_list in TestList.objects.all():
        children = TestList.objects.filter(pk__in=test_list.children.values_list("child__pk", flat=True))
        all_lists = TestList.objects.filter(pk=test_list.pk) | children
        tests = Test.objects.filter(testlistmembership__test_list__in=all_lists).distinct()
        arrs = tests.exclude(autoreviewruleset_id=None).values_list("autoreviewruleset_id", flat=True)
        no_auto_review = len(arrs) == 0
        if no_auto_review:
            continue

        all_have_auto_review = len(arrs) == len(tests)
        rules_all_same = len(set(arrs)) == 1
        uniform_rules = rules_all_same and all_have_auto_review
        if uniform_rules:
            test_list.autoreviewruleset_id = arrs[0]
            test_list.save()
        else:
            msg = (
                f"Tests from Test List '{test_list.name}' did not have uniform auto review rules. "
                "Please set the auto review rule set for this test list manually"
            )
            print(msg)
            logger.warning(msg)


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0062_testlist_autoreviewruleset'),
    ]

    operations = [
        migrations.RunPython(test_arrs_to_test_list_arrs, lambda apps, schema: None),
    ]
