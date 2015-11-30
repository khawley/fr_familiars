import sys


class Echo:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def echo(self, msg, newline=False, verbose=False):
        """
        If verbose, print the msg to stdout.
        :param string msg: String to be printed
        :param bool newline: Whether to add a newline after msg
        :param bool verbose: whether to actually print
        :return:
        """
        if newline:
            msg += "\n"
        if self.verbose or verbose:
            sys.stdout.write(msg)

    def error(self, msg, newline=False, verbose=False):
        """
        If verbose, print the msg to stderr.
        :param string msg: String to be printed
        :param bool newline: Whether to add a newline after msg
        :param bool verbose: whether to actually print
        :return:
        """
        if newline:
            msg += "\n"
        if self.verbose or verbose:
            sys.stderr.write(msg)
