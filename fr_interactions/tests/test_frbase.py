import unittest
from utils import capture_output
from fr_interactions.FrBase import FrBase
from settings import FR_COOKIE


class TestFrBase(unittest.TestCase):
    def setUp(self):
        self.fr_base = FrBase(FR_COOKIE, verbosity=True)
        self.fr_base_muted = FrBase(FR_COOKIE, verbosity=False)
        self.url = "http://flightrising.com/main.php"
        self.ajax_url = "http://flightrising.com/includes/hoard_main.php"

    def test_curl(self):
        fr_base = FrBase(FR_COOKIE, verbosity=True)

        # test get
        response_text = fr_base.curl(self.url)
        self.assertTrue("html" in response_text)

        # test post
        response_text = fr_base.curl(
            # good generic url to test against POST
            "http://www1.flightrising.com/msgs/generic-item-dialog",
            post_data={"slot": 0, "filter": "transmutable"}
        )
        self.assertTrue("div" in response_text)

        # test bad response
        with capture_output() as (out, err):
            with self.assertRaises(SystemExit):
                fr_base.curl("http://flightrising.com/hello-there")
            self.assertIsNotNone(err.getvalue())

    def test_is_logged_in_true(self):
        fr_base = FrBase(FR_COOKIE, verbosity=True)
        response_text = self.fr_base.curl(self.url)
        self.assertTrue(fr_base.is_logged_in(response_text))

        # this tests that returns True, because above already stored logged_in
        self.assertTrue(fr_base.is_logged_in(""))

    def test_is_logged_in_false(self):
        fr_base = FrBase("PHPSESSID", verbosity=True)
        response_text = fr_base.curl(self.url)
        self.assertFalse(fr_base.is_logged_in(response_text))

    def test_is_logged_in_error(self):
        fr_base = FrBase("fr_session", verbosity=True)
        response_text = fr_base.curl(self.url)

        with capture_output() as (out, err):
            self.assertFalse(fr_base.is_logged_in(response_text))
            self.assertTrue(err.getvalue())

    def test_is_logged_in_true_ajax(self):
        fr_base = FrBase(FR_COOKIE, verbosity=True)
        response_text = fr_base.curl(self.ajax_url)
        self.assertTrue(fr_base.is_logged_in(response_text))

    def test_echo(self):
        msg = "hello world"
        with capture_output() as (out, err):
            self.fr_base.echo(msg)
            self.assertEqual(out.getvalue(), msg + " ")
            self.assertFalse(err.getvalue())

        with capture_output() as (out, err):
            self.fr_base.echo(msg, newline=True)
            self.assertEqual(out.getvalue(), msg + "\n")
            self.assertFalse(err.getvalue())

        # muted
        with capture_output() as (out, err):
            self.fr_base_muted.echo(msg)
            self.assertFalse(out.getvalue())
            self.assertFalse(err.getvalue())
        # muted made loud
        with capture_output() as (out, err):
            self.fr_base_muted.echo(msg, verbose=True)
            self.assertEqual(out.getvalue(), msg + " ")
            self.assertFalse(err.getvalue())

    def test_echo_n(self):
        msg = "hello world"
        with capture_output() as (out, err):
            self.fr_base.echo_n(msg)
            self.assertEqual(out.getvalue(), msg + "\n")
            self.assertFalse(err.getvalue())

        with capture_output() as (out, err):
            self.fr_base_muted.echo(msg)
            self.assertFalse(out.getvalue())
            self.assertFalse(err.getvalue())

        with capture_output() as (out, err):
            self.fr_base_muted.echo(msg, verbose=True)
            self.assertEqual(out.getvalue(), msg + " ")
            self.assertFalse(err.getvalue())

    def test_error(self):
        msg = "hello world"
        with capture_output() as (out, err):
            self.fr_base.error(msg)
            self.assertEqual(err.getvalue(), msg)
            self.assertFalse(out.getvalue())

        with capture_output() as (out, err):
            self.fr_base.error(msg, newline=True)
            self.assertEqual(err.getvalue(), msg + "\n")
            self.assertFalse(out.getvalue())

        # muted still announces errors
        with capture_output() as (out, err):
            self.fr_base_muted.error(msg)
            self.assertEqual(err.getvalue(), msg)
            self.assertFalse(out.getvalue())
