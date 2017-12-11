# -*- coding: utf-8 -*-

from .context import wan_test
import wan_test.ping

import platform
import unittest
import logging


class PingTestSuite(unittest.TestCase):
    """Basic ping test cases."""
    def setUP(self):
        pass

    def test_should_reply_OK(self):
        # The ping command is OS-dependent
        ip = "192.168.1.1"
        osid = platform.system().lower()

        # Creates the cmd for Windows/Linux/Mac OS    
        cmd = "ping" + " "
        result = ""
        if osid == "windows":
            pass
        elif osid == "linux" or osid == "darwin":
            cmd = cmd + "-c1" + " "
        else: # The current OS is unsupported yet
            result = "Unsupported OS: " + osid

        self.assertFalse("Unsupported OS" in result,
                         "Error: your OS is not supported yet: " + osid)

        result = wan_test.ping.ping2(1, ip, cmd)
        self.assertTrue("reachable" in result, "Should be found")
        self.assertFalse("NOT reachable" "reachable" in result,
                        "Should not be found")


if __name__ == '__main__':
    unittest.main()
