#!/usr/bin/env python
# coding:utf-8

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
        """Read all the configuration info from file gdeployer.ini."""
        self.config = ConfigParser.RawConfigParser()
        self.config.read('wan_test.ini')

        # appids,  goagent server src dir, Python interpretor & location of GAE appcfg.py
        self.ip_addresses = self.config.get('ping', 'ip_addresses')    

        # appids,  goagent server src dir, Python interpretor & location of GAE appcfg.py
        self.domain_names = self.config.get('nslookup', 'domain_names')
        
        # Email address & 2-step authentication
        self.outbox = self.config.get('email', 'outbox')
        self.inbox = self.config.get('email', 'inbox')
        
        # appids,  goagent server src dir, Python interpretor & location of GAE appcfg.py
        self.portals = self.config.get('portal', 'portals')

        # appids,  goagent server src dir, Python interpretor & location of GAE appcfg.py
        self.web_urls = self.config.get('signin', 'web_urls')
        self.usernames = self.config.get('signin', 'usernames')        
        self.passwords = self.config.get('signin', 'passwords')

    def show_info(self):
        """Display the configuration info to debug."""
        # [gae] section        
        print("ip_addresses = %s" % self.ip_addresses)
        print("domain_names = %s" % self.domain_names)
        print("outbox: %s" % self.outbox)
        print("inbox: %s" % self.inbox)
        print("portals: %s" % self.portals)
        print("web_urls: %s" % self.web_urls)
        print("usernames: %s" % self.usernames)
        print("passwords: %s" % self.passwords)

if __name__ == '__main__':
    gdcp = WANTestConfigParser()
    gdcp.show_info()
    #print("--- Work done!")  
