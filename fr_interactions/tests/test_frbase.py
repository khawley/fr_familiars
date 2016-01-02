import unittest
from fr_interactions.FrBase import FrBase
from settings import FR_COOKIE


class TestBestiary(unittest.TestCase):
    def setUp(self):
        self.url = "http://flightrising.com/main.php"
        self.ajax_url = "http://flightrising.com/includes/hoard_main.php"

    def test_curl(self):
        fr_base = FrBase(FR_COOKIE, verbosity=True)
        response_text = fr_base.curl(self.url)
        self.assertTrue("html" in response_text)

    def test_is_logged_in_true(self):
        fr_base = FrBase(FR_COOKIE, verbosity=True)
        response_text = fr_base.curl(self.url)
        self.assertTrue(fr_base.is_logged_in(response_text))

    def test_is_logged_in_false(self):
        fr_base = FrBase("PHPSESSID", verbosity=True)
        response_text = fr_base.curl(self.url)
        self.assertFalse(fr_base.is_logged_in(response_text))

    def test_is_logged_in_true_ajax(self):
        fr_base = FrBase(FR_COOKIE, verbosity=True)
        response_text = fr_base.curl(self.ajax_url)
        self.assertTrue(fr_base.is_logged_in(response_text))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBestiary)
    unittest.TextTestRunner(verbosity=1).run(suite)