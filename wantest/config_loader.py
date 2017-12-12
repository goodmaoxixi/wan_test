#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# WAN test configuration file test_config.ini parser
# Authors:
#   goodmaoxixi@gmail.com
#   guanglin.du@gmail.com

import os
import re
import ConfigParser

# Versions based on date
__version__ = '20171115a'


# Class to read the configuration info.
class WANTestConfigParser(object):

    def __init__(self):
        """Read all the configuration info from file test_config.ini."""
        self.config = ConfigParser.RawConfigParser()
        self.config.read('wan_test.ini')

        self.ip_addresses = self.config.get('ping', 'ip_addresses')    
        self.domain_names = self.config.get('nslookup', 'domain_names')
        self.portals = self.config.get('portal', 'portals')
        self.web_urls = self.config.get('signin', 'web_urls')
        self.usernames = self.config.get('signin', 'usernames')
        self.passwords = self.config.get('signin', 'passwords')
        
        # Email sending and receiving info
        self.mail_host = self.config.get('email', 'mail_host')
        self.mail_user = self.config.get('email', 'mail_user')
        self.mail_pass = self.config.get('email', 'mail_pass')
        self.mail_postfix = self.config.get('email', 'mail_postfix')
        self.mail_to_list = self.config.get('email', 'mail_to_list')
        self.behind_proxy = self.config.get('email', 'behind_proxy')
        self.proxy_host = self.config.get('email', 'proxy_host')
        self.proxy_port = self.config.get('email', 'proxy_port')
                        
    def show_info(self):
        """Display the configuration info to debug."""
        print("ip_addresses = %s" % self.ip_addresses)
        print("domain_names = %s" % self.domain_names)
        print("portals: %s" % self.portals)
        print("web_urls: %s" % self.web_urls)
        print("usernames: %s" % self.usernames)
        print("passwords: %s" % self.passwords)
        print("mail_host: %s" % self.mail_host)
        print("mail_user: %s" % self.mail_user)
        print("mail_pass: %s" % self.mail_pass)
        print("mail_postfix: %s" % self.mail_postfix)
        print("mail_to_list: %s" % self.mail_to_list)
        print("behind_proxy: %s" % self.behind_proxy)
        print("proxy_host: %s" % self.proxy_host)
        print("proxy_port: %s" % self.proxy_port)
        

if __name__ == '__main__':
    wtcp = WANTestConfigParser()
    wtcp.show_info()
