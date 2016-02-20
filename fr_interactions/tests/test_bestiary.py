import unittest

from fr_interactions.Bestiary import Bestiary
from settings import FR_COOKIE
from data_for_tests import BEASTS, BESTIARY_BREAKDOWN


class TestBestiary(unittest.TestCase):
    def setUp(self):
        self.B = Bestiary(FR_COOKIE, verbosity=True)
        self.B_prepped = Bestiary(FR_COOKIE, verbosity=True)
        self.B_prepped.beasts = BEASTS

    def test_get_one_page(self):
        pass
    
    def test__breakdown_beasts(self):
        self.assertEqual(
            self.B._Bestiary__breakdown_beasts(these_beasts=BEASTS),
            BESTIARY_BREAKDOWN)
        self.assertEqual(
            self.B_prepped._Bestiary__breakdown_beasts(),
            BESTIARY_BREAKDOWN)

    def test_get_beast_by_id(self):
        beast_dict = {'src': u'/images/cms/familiar/art/358.png', 'loyalty': u'Awakened', 'id': u'358', 'name': u'Autumn Dryad'}
        self.assertEqual(
            self.B_prepped.get_beast_by_id("358"),
            beast_dict)

        # beasts_breakdown not initialized yet
        self.assertEqual(
            self.B_prepped.get_beast_by_id("358", "awakened"),
            {})

        # initialize beasts_breakdown
        self.B_prepped.beasts_breakdown = BESTIARY_BREAKDOWN
        self.assertEqual(
            self.B_prepped.get_beast_by_id("358", "awakened"),
            beast_dict)
        self.assertEqual(self.B_prepped.get_beast_by_id("358", "taming"), {})

    def test_get_beast_name_by_id(self):
        beast_name = u'Autumn Dryad'
        self.assertEqual(
            self.B_prepped.get_beast_name_by_id("358"),
            beast_name)

        # beasts_breakdown not initialized yet
        self.assertEqual(
            self.B_prepped.get_beast_name_by_id("358", "awakened"),
            "")

        # initialize beasts_breakdown
        self.B_prepped.beasts_breakdown = BESTIARY_BREAKDOWN
        self.assertEqual(
            self.B_prepped.get_beast_name_by_id("358", "awakened"),
            beast_name)
        self.assertEqual(self.B_prepped.get_beast_name_by_id("358", "taming"), "")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBestiary)
    unittest.TextTestRunner(verbosity=2).run(suite)