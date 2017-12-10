# -*- coding: utf-8 -*-

from .context import wan_test
import wan_test.ping

import unittest


class PingTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_should_reply_OK(self):
        assert True


if __name__ == '__main__':
    unittest.main()
