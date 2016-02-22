import unittest

from mock import patch

from fr_interactions.Bestiary import Bestiary
from fr_interactions.tests.stock_data.stock_vars import BEASTS, BESTIARY_BREAKDOWN
from fr_interactions.tests.stock_data.Bestiary_vars \
    import NOT_LOGGED_IN_BESTIARY_PAGE_1, LOGGED_IN_BESTIARY_PAGE_1, \
    PARSED_BESTIARY_PAGE_1, BEAST_SPAN, PARSED_BEAST_SPAN, BAD_BESTIARY_PAGE, \
    BREAKDOWN_BESTIARY_PAGE_1, BESTIARY_PAGE_1_OF_3, BESTIARY_PAGE_2_OF_3,\
    BESTIARY_PAGE_3_OF_3, BREAKDOWN_PAGE_1_TO_3, \
    PRINT_TAMING_FOR_BESTIARY_BREAKDOWN, PRINT_TAMING_BESTIARY_PAGE__1_TO_3
from settings import FR_COOKIE
from utils import capture_output
from bs4 import BeautifulSoup


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

    def test__get_page__not_logged_in(self):
        with patch.object(Bestiary, 'curl') as mock_curl:
            B = Bestiary("PHPSESSID")

            # not logged in, raises error
            with self.assertRaises(SystemExit):
                mock_curl.return_value = NOT_LOGGED_IN_BESTIARY_PAGE_1
                B._Bestiary__get_page("1")

    def test__get_page__logged_in(self):
        with patch.object(Bestiary, 'curl') as mock_curl:
            B = Bestiary("PHPSESSID")

            mock_curl.return_value = LOGGED_IN_BESTIARY_PAGE_1
            self.assertEqual(B._Bestiary__get_page("1"), PARSED_BESTIARY_PAGE_1)

    def test__parse_beast_span(self):
        tag = BeautifulSoup(BEAST_SPAN, "html.parser").span
        self.assertEqual(self.B._Bestiary__parse_beast_span(tag), PARSED_BEAST_SPAN)

    def test__parse_bestiary_page(self):
        self.assertEqual(self.B._Bestiary__parse_bestiary_page(LOGGED_IN_BESTIARY_PAGE_1), PARSED_BESTIARY_PAGE_1)

        # confirm that the max_bestiary_page is being properly parsed & set
        self.assertEqual(self.B.max_bestiary_page, 52)

        with capture_output() as (out, err):
            self.B._Bestiary__parse_bestiary_page(BAD_BESTIARY_PAGE)
            self.assertTrue(
                err.getvalue().startswith("Error: Parsed out id, but not name - "))

    def test_get_one_page(self):
        with patch.object(Bestiary, "curl") as mock_curl:
            mock_curl.return_value = LOGGED_IN_BESTIARY_PAGE_1
            B = Bestiary("PHPSESSID")
            self.assertEqual(B.get_one_page(1), BREAKDOWN_BESTIARY_PAGE_1)

    def test_get_all(self):
        returns = [BESTIARY_PAGE_1_OF_3, BESTIARY_PAGE_2_OF_3, BESTIARY_PAGE_3_OF_3]

        def side_effects(*args):
            return returns.pop(0)

        with patch.object(Bestiary, "curl") as mock_curl:
            mock_curl.side_effect = side_effects
            B = Bestiary("PHPSESSID")
            self.assertEqual(B.get_all(), BREAKDOWN_PAGE_1_TO_3)
            self.assertEqual(B.max_bestiary_page, 3)

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

    def test_print_beasts_breakdown(self):
        returns = [BESTIARY_PAGE_1_OF_3, BESTIARY_PAGE_2_OF_3, BESTIARY_PAGE_3_OF_3]

        def side_effects(*args):
            return returns.pop(0)

        # pass in a set breakdown
        B = Bestiary("PHPSESSID")
        with capture_output() as (out, err):
            B.print_beasts_breakdown(this_breakdown=BESTIARY_BREAKDOWN)
            self.assertEqual(out.getvalue(),
                             PRINT_TAMING_FOR_BESTIARY_BREAKDOWN)

        # pass in bestiary_breakdown on init
        B = Bestiary("PHPSESSID", bestiary_breakdown=BESTIARY_BREAKDOWN)
        with capture_output() as (out, err):
            B.print_beasts_breakdown()
            self.assertEqual(out.getvalue(),
                             PRINT_TAMING_FOR_BESTIARY_BREAKDOWN)

        # curl bestiary page 1-3, and created the breakdown & printout
        with patch.object(Bestiary, "curl") as mock_curl:
            mock_curl.side_effect = side_effects
            B = Bestiary("PHPSESSID")
            with capture_output() as (out, err):
                B.print_beasts_breakdown()
                self.assertEqual(out.getvalue(),
                                 PRINT_TAMING_BESTIARY_PAGE__1_TO_3)
