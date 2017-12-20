# -*- coding: utf-8 -*-
import unittest

from .context import wantest
import wantest.nslookup


class NSLookupTestSuite(unittest.TestCase):
    """Nslookup test cases."""

    @classmethod
    def setUpClass(cls):
        """Class-scope test fixtures"""
        cls.bing_dot_com = "bing.com"
        #cls.ip = "202.106.46.151" # IP address of bing.com
        cls.ip = "204.79.197.200"

    def test_nslookup(self):
        s1 = wantest.nslookup.resolve_domain_name(self.bing_dot_com)
        self.assertTrue(self.ip in s1, "Should be found")


if __name__ == '__main__':
    unittest.main()
