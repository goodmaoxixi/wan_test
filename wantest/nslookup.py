# Tests whether an IP address is reachable by pinging.
# Created on Oct. 17, 2017 Fri.
# Authors:
#   goodmaoxixi@gmail.com
#   guanglin.du@gmail.com

import socket
import datetime


def resolve_domain_name(domain_name):
    nowStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    s1 = ""
    try:
        s1 = " => " + socket.gethostbyname(domain_name)
    except socket.error, err_msg:
        s1 = ": " + str(err_msg)
    
    result = nowStr + " " + domain_name + s1
    print(result)
    return result


if __name__ == '__main__':
    resolve_domain_name("www.baidu.com")
    resolve_domain_name("www.baidunonexitent.com")
