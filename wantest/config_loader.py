#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# WANTest configuration parser.
# Authors:
#   goodmaoxixi@gmail.com
#   guanglin.du@gmail.com

import os
import re
import ConfigParser

# Versions based on date
__version__ = '20171115a'
    

class WANTestConfigParser(object):
    """Parses the WANTest configuration file wantest.ini."""

    def __init__(self):
        """Read all the configuration info from file test_config.ini."""
        self.config = ConfigParser.RawConfigParser()
        self.config.read('../tmp/wantest.ini') # used in development only      

        self.ip_addresses = self.config.get('ping', 'ip_addresses')    
        self.domain_names = self.config.get('nslookup', 'domain_names')
        self.portals      = self.config.get('portal', 'portals')
        self.web_urls     = self.config.get('signin', 'web_urls')
        self.usernames    = self.config.get('signin', 'usernames')
        self.passwords    = self.config.get('signin', 'passwords')
        
        # Email sending and receiving info
        self.smtp_host    = self.config.get('email', 'smtp_host')
        self.mail_port    = self.config.get('email', 'mail_port')
        self.use_ssl    = self.config.get('email', 'use_ssl')
        self.mail_user    = self.config.get('email', 'mail_user')
        self.mail_pass    = self.config.get('email', 'mail_pass')
        self.mail_postfix = self.config.get('email', 'mail_postfix')
        self.mail_to_list = self.config.get('email', 'mail_to_list')
        self.behind_proxy = self.config.getint('email', 'behind_proxy')
        self.proxy_host   = self.config.get('email', 'proxy_host')
        self.proxy_port   = self.config.getint('email', 'proxy_port')
                        
    def show_info(self):
        """Display the configuration info to debug."""
        print("--- ping ---")
        print("ip_addresses: {0}".format(self.ip_addresses))
        print("\n--- nslookup ---")
        print("domain_names: {0}".format(self.domain_names))
        print("portals: {0}".format(self.portals))
        print("\n--- email ---")
        print("smtp_host: {0}".format(self.smtp_host))
        print("use_ssl: {0}".format(self.use_ssl))
        print("mail_port: {0}".format(self.mail_port))
        print("mail_user: {0}".format(self.mail_user))
        print("mail_pass: {0}".format(self.mail_pass))
        print("mail_postfix: {0}".format(self.mail_postfix))
        print("mail_to_list: {0}".format(self.mail_to_list))
        print("behind_proxy: {0}".format(self.behind_proxy))
        print("proxy_host: {0}".format(self.proxy_host))
        print("proxy_port: {0}".format(self.proxy_port))
        print("\n--- signin ---")
        print("web_urls: {0}".format(self.web_urls))
        print("usernames: {0}".format(self.usernames))
        print("passwords: {0}".format(self.passwords))
        

if __name__ == '__main__':
    # Forces the start dir is where this file resides.    
    __file__ = os.path.abspath(__file__)
    if os.path.islink(__file__):
        __file__ = getattr(os, 'readlink', lambda x: x)(__file__)
    work_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(work_path)

    wtcp = WANTestConfigParser()
    wtcp.show_info()
