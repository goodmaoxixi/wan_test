# Tests whether an IP address is reachable by pinging.
# Created on Oct. 12, 2017 Thu.
# Modified on Oct 16, Mon.
# Authors:
#   goodmaoxixi@gmail.com
#   guanglin.du@gmail.com

import os
import shlex
import datetime
import subprocess
import ping
import test_url
import send_email
import test_config_parser

# A global variable to hold the test configuration.
tcp = test_config_parser.WANTestConfigParser()


def ping_addresses():
    addresses = tcp.ip_addresses.split("|")
    #for address in addresses:
    result = ping.pingsite(addresses, out)
        #pass


def test_DNS():
    domain_names = tcp.domain_names.split("|")
    for name in domain_names:
        pass


def test_portals():
    portals = tcp.portals.split("|")
    for portal in portals:
        result = test_url.is_url_accessible(portal)
        f = open(out, "a+")
        f.write(result + "\n")
        f.close()
        # Outputs to a file.


def test_email():
    """ Only sends an email. Please check your inbox manually."""
    mail_to_list = [tcp.mail_to_list] # converts to an array
    nowStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    news = "Hello, World!\n--- Automatically sent from the WAN test suite."
    if send_email.send(tcp.mail_host, tcp.mail_user, tcp.mail_pass,
                                    tcp.mail_postfix, mail_to_list, nowStr, news): 
        print(now + " Mail sent successfully")
    else: 
	    print(now + " Failed sending the email!!! Please check your settings.")


if __name__ == "__main__":
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    print("A string format time %s" % now)
	
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nowtime = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    out = "./tmp/result-" + str(nowtime) + ".txt"
    print out
    #file_object = open(out, "w+")
    print("\n*** WAN test started at " + now + " ***")
    ping_addresses()
    test_DNS()
    test_portals()
    test_email()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("*** WAN test ended at " + now + " ***\n")
