#!/usr/bin/env python
# coding:utf-8

# The main entry of this WANTest suite. Since the working dir will be changed
# internally, this script can be started from anywhere.
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

# Forces the start dir is where this file resides.    
__file__ = os.path.abspath(__file__)
if os.path.islink(__file__):
    __file__ = getattr(os, 'readlink', lambda x: x)(__file__)
work_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(work_path)

# A global variable to hold the test configuration.
wtcp = config_loader.WANTestConfigParser()
# The ping command is OS-dependent
osid = platform.system().lower()


def ping_addresses(output_file):
    # Outputs the reachable addresses
    output_file.write("\n*** ping tests started ***\n")
    # Creates the cmd for Windows/Linux/Mac OS    
    cmd = "ping "
    if osid == "windows":
        pass
    elif osid == "linux" or osid == "darwin":
        cmd = cmd + "-c1 "
    else: # exits if the OS is not supported yet
        result = "Unknown OS: " + osid + " I don't know how to ping."
        output_file.write(result)        
        print(result)
        output_file.write("*** ping tests ended with errors ***\n")
        print("*** ping tests ended with errors ***\n")
        return result
    
    addresses = wtcp.ip_addresses.split("|")
    print("\n*** ping tests started ***")
    for count, ip in enumerate(addresses):
        cmd = cmd + " " + ip
        result = ping.ping2(count, cmd)
        output_file.write(result)

    output_file.write("*** ping tests ended ***\n")
    print("*** ping tests ended ***\n")


def test_DNS(output_file):
    domain_names = wtcp.domain_names.split("|")
    print("*** nslookup tests started ***")
    output_file.write("\n\n*** nslookup tests started ***\n")
    nowStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for name in domain_names:
        result = nslookup.resolve_domain_name(name)
        output_file.write(nowStr + " " + result + "\n")
    output_file.write("*** nslookup tests ended ***\n")
    print("*** nslookup tests ended ***\n")


def test_portals(output_file):
    portals = wtcp.portals.split("|")
    print("*** portal tests started ***")
    output_file.write("\n\n*** portal tests started ***\n")
    for portal in portals:
        result = access_url.is_url_accessible(portal)
        output_file.write(result + "\n")
    output_file.write("*** portal tests ended ***\n")
    print("*** portal tests ended ***\n")


def test_email(output_file):
    """ Only sends an email. Please check your inbox manually."""
    mail_to_list = [wtcp.mail_to_list] # converts to an array
    nowStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    news = "Hello, World!\n--- Automatically sent from the WAN test suite."
    
    print("*** Email tests started ***\n")
    output_file.write("\n\n*** email tests started ***\n")
    msg = (nowStr + " "
          + wtcp.mail_user + "@" + wtcp.mail_postfix
          + " sent "
          + wtcp.mail_to_list)

    if wtcp.behind_proxy == 0: # no proxy
        if send_email.send(
                 wtcp.smtp_host,
                 wtcp.mail_user,
                 wtcp.mail_pass,
                 wtcp.mail_postfix,
                 wtcp.mail_to_list,
                 nowStr,
                 news):
            msg = msg + " an email successfully.\n"
            print(msg)
            output_file.write(msg)
        else:
            msg = msg + " an email UNsuccessfully.\n"    
            print(msg)
            output_file.write(msg)
    else: # behind a proxy
        if send_email.send_behind_proxy(
                wtcp.smtp_host,
                wtcp.mail_port,
                wtcp.proxy_host,
                wtcp.proxy_port,
                wtcp.mail_user,
                wtcp.mail_pass,
                wtcp.mail_postfix,
                wtcp.mail_to_list):
            msg = msg + " an email behind proxy successfully.\n"
            print(msg)
            output_file.write(msg)
        else:
            msg = msg + " an email behind proxy UNsuccessfully.\n"    
            print(msg)
            output_file.write(msg)

    output_file.write("*** Email tests ended ***\n")
    print("*** Email tests ended ***\n")


# TODO: To be implemented.
def test_signin(output_file):
    output_file.write("\n!!!Signin tests not supported yet."
                      +" Please do that manually.\n")


def println(s, file=sys.stderr):
	assert type(s) is type(u'')
	file.write(s.encode(sys.getfilesystemencoding(), 'replace') + os.linesep)


if __name__ == "__main__":
    #now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    #print("A string format time %s" % now)	
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    now2 = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = "../tmp/result-" + str(now2) + ".txt"
    output_file = open(filename, "w+")

    print("\n=== WAN test started at " + now + " ===")
    println(u'''~~~ 广域网应急演练自动测试脚本 ~~~'''.strip())        
    ping_addresses(output_file)
    test_DNS(output_file)
    test_portals(output_file)
    test_email(output_file)
    test_signin(output_file)
    output_file.close()

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n!!!Signin tests not supported yet. Please do that manually.")
    println(u'''网站登录测试尚不支持，请手动执行！'''.strip())    
    print("=== WAN test ended at " + now + " ===\n")
    println(u'''~~~ 测试脚本运行结束，请到tmp目录下查看结果。 ~~~'''.strip())   
    
