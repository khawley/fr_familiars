import unittest
from fr_interactions.DragonLair import DragonLair
from fr_interactions.tests.stock_data.DragonLair_vars import DRAGON_LAIR_PAGE_1, DRAGON_PAGE_GEMSTONE, DRAGON_PAGE_UNNAMED, DRAGON_LAIR_ID, GEMSTONE_ID, GEMSTONE_FAMILIAR_ID, UNNAMED_ID, DRAGONS_FROM_LAIR_PAGE_1
from settings import FR_COOKIE
from mock import patch


class TestDragonLair(unittest.TestCase):

    def setUp(self):
        self.D = DragonLair(DRAGON_LAIR_ID, FR_COOKIE)

    def test__parse_dragon_page(self):
        # check that the return is the familiar id
        self.assertEqual(
            self.D._DragonLair__parse_dragon_page(DRAGON_PAGE_GEMSTONE),
            GEMSTONE_FAMILIAR_ID)

        # check that a dragon page w/o familiar returns empty string
        self.assertEqual(
            self.D._DragonLair__parse_dragon_page(DRAGON_PAGE_UNNAMED),
            "")

    def test__get_dragon_famliar_id(self):
        # check that the return is the familiar id
        with patch.object(DragonLair, 'curl') as mock_curl:
            mock_curl.return_value = DRAGON_PAGE_GEMSTONE
            self.assertEqual(
                self.D._DragonLair__get_dragon_familiar_id(GEMSTONE_ID),
                GEMSTONE_FAMILIAR_ID)

            # check that a dragon page w/o familiar returns empty string
            mock_curl.return_value = DRAGON_PAGE_UNNAMED
            self.assertEqual(
                self.D._DragonLair__get_dragon_familiar_id(UNNAMED_ID),
                "")

    def test__parse_lair_page(self):
        D = DragonLair(DRAGON_LAIR_ID, FR_COOKIE)
        # TODO: need to add mock_curl for each dragon on the lair page

        D._DragonLair__parse_lair_page(DRAGON_LAIR_PAGE_1)
        self.assertEqual(D.dragons, DRAGONS_FROM_LAIR_PAGE_1)

        pass

        # check that the self.dragons got all the dragons on the page
