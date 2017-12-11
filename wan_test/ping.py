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
import datetime
import subprocess


def ping1(count, ip, cmd):
    """The 1st simple implementation."""	
    for count, ip in enumerate(addresses):
        if os.system("ping -c 1 " + ip ) == 0:# Linux
            print("%d. %s is up." % (count, ip))
            #output_file.write(ip + "\n")
	    #elsif os.system("ping " + ip ) == 0:# Windows
        else:
            print("%d. %s is down." % (count, ip))	

		
def ping2(count, ip, cmd):
    """The 2nd implementation, a better one."""
    result = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Tokenizes the shell command.
    cmd = shlex.split(cmd + ip) # Windows/Linux		
    
    s1 = "reachable."
    try:
        output = subprocess.check_output(cmd)
    except subprocess.CalledProcessError,e:
        s1 = "NOT reachable."
    else:
        pass

    result = (result + " "
              + str(count) + " "
              + "The IP address {0} is".format(cmd[-1]) + " "
              + s1)
    return result
