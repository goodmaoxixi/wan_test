# Tests whether a wan test IP address is reachable by pinging.
# Created on Oct. 12, 2017 Thu.
# Modified on Oct 16, Mon.

# See
# https://stackoverflow.com/questions/25842744/ping-to-a-specific-ip-address-using-python

import os
import shlex
import subprocess
import ping


# Loads the configuration info

		
if __name__ == "__main__":	
    # Contains the wan test IP addresses
    #addresses = contents.splitlines()
    # Removes the empty lines
    #addresses = ' '.join(addresses).split()
    #print addresses
    ping.pingsite()
