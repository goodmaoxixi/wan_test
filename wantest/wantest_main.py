#!/usr/bin/env python
# coding:utf-8

# Tests whether an IP address is reachable by pinging.
# Created on Oct. 12, 2017 Thu.
# Authors:
#   goodmaoxixi@gmail.com
#   guanglin.du@gmail.com

import os
import sys
import shlex
import datetime
import platform
import subprocess

import ping
import access_url
import nslookup
import send_email
import config_loader


# A global variable to hold the test configuration.
wtcp = config_loader.WANTestConfigParser()
# The ping command is OS-dependent
osid = platform.system().lower()


def ping_addresses(filename):
    # Outputs the reachable addresses
    f = open(filename, "w+")
    f.write("\n*** ping tests started ***\n")

    # Creates the cmd for Windows/Linux/Mac OS    
    cmd = "ping "
    if osid == "windows":
        pass
    elif osid == "linux" or osid == "darwin":
        cmd = cmd + "-c1 "
    else: # exits if the OS is not supported yet
        result = "Unknown OS: " + osid + " I don't know how to ping."
        f.write(result)        
        print(result)
        f.write("*** ping tests ended with errors ***\n")
        f.close()
        print("*** ping tests ended with errors ***\n")
        return result
    
    addresses = wtcp.ip_addresses.split("|")
    print("\n*** ping tests started ***")
    for count, ip in enumerate(addresses):
        cmd = cmd + " " + ip
        result = ping.ping2(count, cmd)
        f.write(result)

    f.write("*** ping tests ended ***\n")
    f.close()
    print("*** ping tests ended ***\n")


def test_DNS(filename):
    domain_names = wtcp.domain_names.split("|")
    print("*** nslookup tests started ***")
    f = open(filename, "a+")    
    f.write("\n\n*** nslookup tests started ***\n")
    nowStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for name in domain_names:
        result = nslookup.resolve_domain_name(name)
        f.write(nowStr + " " + result + "\n")
    f.write("*** nslookup tests ended ***\n")
    f.close()
    print("*** nslookup tests ended ***\n")


def test_portals(filename):
    portals = wtcp.portals.split("|")
    print("*** portal tests started ***")
    f = open(filename, "a+")    
    f.write("\n\n*** portal tests started ***\n")
    for portal in portals:
        result = test_url.is_url_accessible(portal)
        f = open(filename, "a+")
        f.write(result + "\n")
    f.write("*** portal tests ended ***\n")
    f.close()
    print("*** portal tests ended ***\n")


def test_email(filename):
    """ Only sends an email. Please check your inbox manually."""
    mail_to_list = [wtcp.mail_to_list] # converts to an array
    nowStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    news = "Hello, World!\n--- Automatically sent from the WAN test suite."
    
    print("*** email tests started ***\n")
    f = open(filename, "a+")    
    f.write("\n\n*** email tests started ***\n")
    msg = (nowStr + "\n"
          + wtcp.mail_user + "@" + wtcp.mail_host
          + " sent "
          + wtcp.mail_to_list)

    if send_email.send(wtcp.mail_host, wtcp.mail_user, wtcp.mail_pass,
                       wtcp.mail_postfix, mail_to_list, nowStr, news):
        msg = msg + " an email successfully.\n"
        print(msg)
        f.write(msg)
    else:
        msg = msg + " an email UNsuccessfully.\n"    
        print(msg)
        f.write(msg)
        
    f.write("*** email tests ended ***\n")
    f.write("\n!!!Signin tests not supported yet. Please do that manually.\n")
    f.wtcpose()
    print("*** email tests ended ***\n")

    
def println(s, file=sys.stderr):
	assert type(s) is type(u'')
	file.write(s.encode(sys.getfilesystemencoding(), 'replace') + os.linesep)


if __name__ == "__main__":
    #now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    #print("A string format time %s" % now)	
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    now2 = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = "../tmp/result-" + str(now2) + ".txt"

    print("\n=== WAN test started at " + now + " ===")
    println(u'''~~~ 广域网应急演练自动测试脚本 ~~~'''.strip())        
    ping_addresses(filename)
    test_DNS(filename)
    test_portals(filename)
    test_email(filename)
    
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n!!!Signin tests not supported yet. Please do that manually.")
    println(u'''网站登录测试尚不支持，请手动执行！'''.strip())    
    print("=== WAN test ended at " + now + " ===\n")
    println(u'''~~~ 测试脚本运行结束，请到tmp目录下查看结果。 ~~~'''.strip())   
    
