import unittest

from mock import patch

from fr_interactions.Bestiary import Bestiary
from fr_interactions.tests.stock_data.stock_vars import BEASTS, BESTIARY_BREAKDOWN
from fr_interactions.tests.stock_data.CurlBestiaryResponses import NOT_LOGGED_IN_BESTIARY_PAGE_1
from settings import FR_COOKIE
from utils import capture_output


class TestBestiary(unittest.TestCase):
    def setUp(self):
        self.B = Bestiary(FR_COOKIE, verbosity=True)
        self.B_prepped = Bestiary(FR_COOKIE, verbosity=True)
        self.B_prepped.beasts = BEASTS

    def test__init__(self):
        B = Bestiary(FR_COOKIE, bestiary_breakdown=BESTIARY_BREAKDOWN)

        # confirm that bestiary_breakdown was saved in the class
        self.assertEqual(B.beasts_breakdown, BESTIARY_BREAKDOWN)

        # confirm self.beasts was created from the bestiary breakdown
        self.assertEqual(B.beasts.sort(), BEASTS.sort())

    def test__get_page(self):
        with patch.object(Bestiary, 'curl') as mock_curl:
            B = Bestiary("PHPSESSID")

            # not logged in, raises error
            with self.assertRaises(SystemExit):
                mock_curl.return_value = NOT_LOGGED_IN_BESTIARY_PAGE_1
                B._Bestiary__get_page("1")

    def test_get_one_page(self):
        pass
    
    def test__breakdown_beasts(self):
        self.assertEqual(
            self.B._Bestiary__breakdown_beasts(these_beasts=BEASTS),
            BESTIARY_BREAKDOWN)
        self.assertEqual(
            self.B_prepped._Bestiary__breakdown_beasts(),
            BESTIARY_BREAKDOWN)

        # not initialized with beasts, and none to breakdown,
        # will error and return empty
        with capture_output() as (out, err):
            self.assertEqual(self.B._Bestiary__breakdown_beasts(), None)
            sys_stderr = err.getvalue()
            self.assertEqual(sys_stderr,
                             "Error: No lists of beasts to breakdown")

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

    def test_get_beast_by_name(self):
        beast_dict = {'src': u'/images/cms/familiar/art/1779_gray.png', 'loyalty': u'Locked', 'id': u'1779', 'name': u'Arcane Sprite'}
        self.assertEqual(
            self.B_prepped.get_beast_by_name(beast_dict['name']),
            beast_dict)

        # beasts_breakdown not initialized yet
        self.assertEqual(
            self.B_prepped.get_beast_by_name(beast_dict['name'], "locked"),
            {})

        # initialize beasts_breakdown
        self.B_prepped.beasts_breakdown = BESTIARY_BREAKDOWN
        self.assertEqual(
            self.B_prepped.get_beast_by_name(beast_dict['name'], "locked"),
            beast_dict)
        self.assertEqual(
            self.B_prepped.get_beast_by_name(beast_dict['name'], "awakened"),
            {})

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

    def test__get_beast_by_field_with_src(self):
        beast_dict = {'src': u'/images/cms/familiar/art/13435.png', 'loyalty': u'Relaxed', 'id': u'13435', 'name': u'Almandine Sturgeon'}

        get_beast_by_field = self.B_prepped._Bestiary__get_beast_by_field
        self.assertEqual(
            get_beast_by_field('src', beast_dict['src']),
            beast_dict)

        # beasts_breakdown not initialized yet
        self.assertEqual(
            get_beast_by_field('src', beast_dict['src'], 'taming'),
            {})

        # initialize beasts_breakdown
        self.B_prepped.beasts_breakdown = BESTIARY_BREAKDOWN
        get_beast_by_field = self.B_prepped._Bestiary__get_beast_by_field
        self.assertEqual(
            get_beast_by_field('src', beast_dict['src'], 'taming'),
            beast_dict)
        self.assertEqual(
            get_beast_by_field('src', beast_dict['src'], 'locked'),
            {})
