# -*- coding: utf-8 -*-

from .context import wan_test

import unittest


class NSLookupTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_nslookup_OK(self):
        self.assertIsNone(None)


if __name__ == '__main__':
    unittest.main()
