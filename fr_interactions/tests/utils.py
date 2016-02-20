import sys
from contextlib import contextmanager
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


@contextmanager
def capture_output():
    """
    Helper function to capture stdout & stderr for testing purposes

    Example:
        with captured_output() as (out, err):
            foo()
            output = out.get_value()
            err_out = err.get_value()

    :yeilds: sys.stdout, sys.stderr
    """
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err
