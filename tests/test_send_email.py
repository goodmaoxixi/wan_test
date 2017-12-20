# -*- coding: utf-8 -*-
# Python unittest Fixtures:
# https://dmorgan.info/posts/python-unittest-fixtures/

import platform
import unittest
import datetime

from .context import wantest
import wantest.send_email


class SendMailTestSuite(unittest.TestCase):
    """Mail sending test cases."""

    @classmethod
    def setUpClass(cls):
        """Class-scope test fixtures"""
        cls.smtp_host    = "smtp.example.com"
        cls.use_ssl      = 0
        cls.mail_port    = 25 # 465
        cls.mail_user    = "foo"
        cls.mail_pass    = "password"
        cls.mail_postfix = "example.com"
        cls.mail_to_list = "example@example.com"
        cls.proxy_host   = "192.168.1.1"
        cls.proxy_port   = 8080

    @classmethod
    def tearDownClass(cls):
        pass

    def test_send_email(self):
        nowStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        news = "Hello, World!\n---Automatically sent from the WAN test suite."
        msg = (nowStr + "\n"
               + self.mail_user + "@" + self.smtp_host
               + " sent "
               + self.mail_to_list)
        result = wantest.send_email.send(
            self.smtp_host,
            self.mail_user,
            self.mail_pass,
            self.mail_postfix,
            self.mail_to_list,
            nowStr,
            news)
        self.assertFalse(result, "Should be false as the address is invalid")
        #self.assertTrue(result, "Should be true")

    def test_send_email_behind_proxy(self):        
        result = wantest.send_email.send_behind_proxy(
            self.smtp_host,
            self.mail_port,
            self.proxy_host,
            self.proxy_port,
            self.mail_user,
            self.mail_pass,
            self.mail_postfix,
            self.mail_to_list)
        self.assertTrue("Mail sent successfully" in result,
                        "Successful sending expected")
        

if __name__ == '__main__':
    unittest.main()
