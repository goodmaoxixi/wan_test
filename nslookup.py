
import socket

def resolve_domain_name(domain_name):
    #print("--- Retrieving a remote machine's IP address ---")
    result = domain_name
    try:
        result = result + " => " + socket.gethostbyname(domain_name)
    except socket.error, err_msg:
        result = result + ": " + str(err_msg)
        
    print(result)
    return result
    
    
if __name__ == '__main__':
    resolve_domain_name("www.baidu.com")
    resolve_domain_name("www.baidunonexitent.com")
