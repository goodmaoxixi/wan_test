# Tests whether a wan test IP address is reachable by pinging.
# Created on Oct. 12, 2017 Thu.
# Modified on Oct 16, Mon.

# The ping implementation is based on the following:
# https://stackoverflow.com/questions/25842744/ping-to-a-specific-ip-address-using-python

# String Formatting with the { } Operators &
# Operator % will be deprecated in Python 3.1 & above:
# http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python

import os
import re
import sys
import shlex
import datetime
import subprocess


def ping1(count, cmd):
    """The 1st simple implementation."""
    cmd_list = shlex.split(cmd)
    result = "{0}. {1} is".format(count, cmd_list[-1])
    if os.system(cmd) == 0:
        result = result + " up."
    else:
        result = result + " down."

    return result

		
def ping2(count, cmd):
    """The 2nd implementation, a better one."""
    result = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Tokenizes the shell command.
    cmd = shlex.split(cmd)		
    
    s1 = "reachable."
    try:
        subprocess.check_output(cmd)
    except subprocess.CalledProcessError, e:
        s1 = "NOT reachable."
    else:
        pass

    result = (result + " "
              + str(count) + " "
              + "The IP address {0} is".format(cmd[-1]) + " "
              + s1)
    return result
