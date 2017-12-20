# -*- coding: utf-8 -*-
import unittest

from .context import wantest
import wantest.access_url


class AccessURLTestSuite(unittest.TestCase):
    """URL test cases."""

    @classmethod
    def setUpClass(cls):
        """Class-scope test fixtures"""
        cls.bing_dot_com = "http://www.bing.com"

    def test_url_access(self):
        result = wantest.access_url.is_url_accessible(self.bing_dot_com)
        self.assertTrue(result, "Should be true")


if __name__ == '__main__':
    unittest.main()
