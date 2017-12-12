# -*- coding: utf-8 -*-
# Python unittest Fixtures:
# https://dmorgan.info/posts/python-unittest-fixtures/

import platform
import unittest

from .context import wantest
import wantest.ping


class PingTestSuite(unittest.TestCase):
    """Basic ping test cases."""

    @classmethod
    def setUpClass(cls):
        """Class-scope test fixtures"""
        #cls.ip = "10.0.0.1"
        cls.ip = "10.122.4.10"
        cls.osid = platform.system().lower()
        # The ping command is OS-dependent
        # Creates the cmd for Windows/Linux/Mac OS    
        cls.cmd = "ping" + " "
        cls.result = ""
        if cls.osid == "windows":
            pass
        elif cls.osid == "linux" or cls.osid == "darwin":
            cls.cmd = cls.cmd + "-c1" + " "
        else: # The current OS is unsupported yet
            cls.result = "Unsupported OS: " + cls.osid

    @classmethod
    def tearDownClass(cls):
        pass

    def test_ping1(self):
        # Tests whether your OS is supported
        self.assertFalse("Unsupported OS" in self.result,
                         "Error: your OS is not supported yet: " + self.osid)
        cmd = self.cmd + self.ip
        result = wantest.ping.ping1(1, cmd)
        self.assertTrue("up" in result,    "Should be up")
        self.assertFalse("down" in result, "Should be down")

    def test_ping2(self):        
        # Tests whether your OS is supported
        self.assertFalse("Unsupported OS" in self.result,
                         "Error: your OS is not supported yet: " + self.osid)

        cmd = self.cmd + self.ip
        result = wantest.ping.ping2(1, cmd)
        self.assertTrue("reachable" in result,      "Should be found")
        self.assertFalse("NOT reachable" in result, "Should not be found")


if __name__ == '__main__':
    unittest.main()
