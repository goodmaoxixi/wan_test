# Tests whether a wan test IP address is reachable by pinging.
# Created on Oct. 12, 2017 Thu.
# Modified on Oct 16, Mon.

# See
# https://stackoverflow.com/questions/25842744/ping-to-a-specific-ip-address-using-python

import os
import re
import sys
import shlex
import shutil
import platform
import datetime
import subprocess

# Setp 2: Create the cmd to SET(Windows)/export(Unix/Linux/Mac OS) 
osid = platform.system().lower()


def ping1(addresses, output_file):
    """The 1st simple implementation."""	
    for count, ip in enumerate(addresses):
        if os.system("ping -c 1 " + ip ) == 0:# Linux
		#if os.system("ping " + ip ) == 0:# Windows
            print("%d. %s is up." % (count, ip))
            output_file.write(ip + "\n")
        else:
            print("%d. %s is down." % (count, ip))	

		
def ping2(addresses, output_file):
    cmd = "ping "
    if osid == "windows":
	    pass
    elif osid == "linux" or osid == "darwin":
        cmd = cmd + "-c1 "
    else: # exits abnormally
        print("Unknown OS id: %s. Terminated." % osid)
        return

    """The 2nd implementation, a better one."""
    for count, ip in enumerate(addresses):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cmd = "ping "
	    # Tokenizes the shell command.
        cmd = shlex.split(cmd + ip) # Windows/Linux		
        try:
            output = subprocess.check_output(cmd)
        except subprocess.CalledProcessError,e:
            # Prints the failed command with its exit status
            print(now + "%d The IP address {0} is NOT reachable.".format(cmd[-1]) % count)
            output_file.write(now + " " + ip + " is NOT active.\n")
        else:
            print(now + "%d The IP address {0} is reachable.".format(cmd[-1]) % count)
            output_file.write(now + " " + ip + " is active.\n")

def pingsite(addresses, filename):
    # Which ping method to use?
    #simple_ping = True
    simple_ping = False

    # Outputs the reachable addresses
    f = open(filename, "w+")
    f.write("\n*** ping tests started ***\n")
    if simple_ping:
        ping1(addresses, f)
    else:
        ping2(addresses, f)
    f.write("*** ping tests ended ***\n")
    f.close()
