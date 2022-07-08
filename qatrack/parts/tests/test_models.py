from django.test import TestCase

from qatrack.service_log.tests import utils as sl_utils
from qatrack.units.tests import utils as u_utils


class TestPart(TestCase):

    def setUp(self):

        self.p_1 = sl_utils.create_part(alt_part_number='112358', name='13')

    def test_str(self):
        self.assertEqual(
            str(self.p_1),
            '%s (%s) - %s' % (self.p_1.part_number, self.p_1.alt_part_number, self.p_1.name),
        )


class TestPartStorageCollection(TestCase):

    def setUp(self):
        self.p_1 = sl_utils.create_part()
        self.si_1 = u_utils.create_site()
        self.r_1 = u_utils.create_room(site=self.si_1)
        self.st_1 = u_utils.create_storage(room=self.r_1, location='nowhere')
        self.psc_1 = sl_utils.create_part_storage_collection(part=self.p_1, storage=self.st_1, quantity=1000)

    def test_str(self):
        self.assertEqual(
            str(self.psc_1), '%s - %s - %s - (%s)' % (self.si_1.name, self.r_1.name, self.st_1.location, 1000)
        )
