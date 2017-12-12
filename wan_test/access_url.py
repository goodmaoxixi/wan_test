# Module to test whether a URL is accessible.
# Created on Nov. 15, 2017 Wed.
# Authors:
#   goodmaoxixi@gmail.com
#   guanglin.du@gmail.com

import re
import socket
import httplib
import urllib2
import datetime


# http://stackoverflow.com/questions/1949318/checking-if-a-website-is-up-via-python
def is_website_online(host):
    """
    This function checks to see if a host name has a DNS entry by checking
    for socket info. If the website gets something in return, 
    we know it's available to DNS.
    """
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        return False
    else:
        return True


def is_page_available(host, path="/"):
    """
    This function retreives the status code of a website by requesting
    HEAD data from the host. This means that it only requests the headers.
    If the host cannot be reached or something else goes wrong, it returns
    False.
    """
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        print("Return code: %d" % conn.getresponse().status)        
        if re.match("^[23]\d\d$", str(conn.getresponse().status)):
			return True
    except StandardError:
        return None


# https://gist.github.com/fedir/5883651
def is_url_accessible(url):
    """Tests whether a URL is accessable. This is concise and effective."""
    ret = urllib2.urlopen(url)
    result = ""
    if ret.code == 200:
        result = " is accessable"
    else:
        result = " is NOT accessable"
    
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    result = now + " " + url + result
    print("%s" % result)
    return result


if __name__ == '__main__':
    url = "http://www.baidu.com"
    #if is_website_online(url):
	#    print("%s has a DNS entry" % url)
    result = is_url_accessible(url)   
