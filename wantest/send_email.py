# -*- coding: UTF-8 -*-
# Email-sending module based on my colleague Xuleo's work.
# Authors:
#   xuleo@gmail.com
#   goodmaoxixi@gmail.com
#   guanglin.du@gmail.com

import socket
import smtplib
import datetime
from email.mime.text import MIMEText


def send(mail_host, mail_user, mail_pass,
         mail_postfix, to_list, sub, content): 
    """Sends an email with no proxy."""
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content) 
    msg['Subject'] = sub 
    msg['From'] = me 
    msg['To'] = ";".join(to_list) 
    try: 
        #s = smtplib.SMTP()  # http
        s = smtplib.SMTP_SSL(mail_host, 465) # smtp ssl/Port 465
        s.set_debuglevel(1)
        s.login(mail_user + "@" + mail_postfix, mail_pass) 
        s.sendmail(me, to_list, msg.as_string()) 
        s.quit()
        return True
    except Exception, e: 
        print str(e) 
        return False


def recvline(sock):
    """Sends an email behind a proxy. Receives a line."""
    stop = 0
    line = ''
    while True:
        i = sock.recv(1)
        if i.decode('UTF-8') == '\n': stop = 1
        line += i.decode('UTF-8')
        if stop == 1:
            print('Stop reached.')
            break
    print('Received line: %s' % line)
    return line


class ProxySMTP(smtplib.SMTP):
    """Connects to a SMTP server through an HTTP proxy."""

    def __init__(self, host='', port=0, p_address='',p_port=0,
                 local_hostname=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        """
        Initializes a ProxySMTP instance.

        If specified, `host' is the name of the remote host to which to
        connect.  If specified, `port' specifies the port to which to connect.
        By default, smtplib.SMTP_PORT is used.  An SMTPConnectError is raised
        if the specified `host' doesn't respond correctly.  If specified,
        `local_hostname` is used as the FQDN of the local host.  By default,
        the local hostname is found using socket.getfqdn().
        """
        self.p_address = p_address
        self.p_port = p_port
        self.timeout = timeout
        self.esmtp_features = {}
        self.default_port = smtplib.SMTP_PORT

        if host:
            (code, msg) = self.connect(host, port)
            if code != 220:
                raise IOError(code, msg)

        if local_hostname is not None:
            self.local_hostname = local_hostname
        else:
            # RFC 2821 says we should use the fqdn in the EHLO/HELO verb, and
            # if that can't be calculated, that we should use a domain literal
            # instead (essentially an encoded IP address like [A.B.C.D]).
            fqdn = socket.getfqdn()

            if '.' in fqdn:
                self.local_hostname = fqdn
            else:
                # We can't find an fqdn hostname, so use a domain literal
                addr = '127.0.0.1'
                try:
                    addr = socket.gethostbyname(socket.gethostname())
                except socket.gaierror:
                    pass
                self.local_hostname = '[%s]' % addr

        smtplib.SMTP.__init__(self)

    def _get_socket(self, port, host, timeout):
        # This makes it simpler for SMTP to use the SMTP connect code
        # and just alter the socket connection bit.
        print('Will connect to:', (host, port))
        print('Connect to proxy.')
        new_socket = socket.create_connection((self.p_address, self.p_port),
                                              timeout)
        s = "CONNECT %s:%s HTTP/1.1\r\n\r\n" % (port, host)
        s = s.encode('UTF-8')
        new_socket.sendall(s)

        print('Sent CONNECT. Receiving lines.')
        for x in range(2): recvline(new_socket)

        print('Connected.')
        return new_socket


def send_behind_proxy(host, port, p_address, p_port, mail_user, mail_pass,
                      mail_postfix, receivers):
    """Email receivers must be a list object, e.g., ["312@qq.com"]"""
    # Both port 25 and 587 work for SMTP
    conn = ProxySMTP(host, port, p_address, p_port)
    conn.ehlo()
    conn.starttls()
    conn.ehlo()

    sender = mail_user + "@" + mail_postfix    
    msg = """From: From Person <from@fromdomain.com>
             To: To Person <to@todomain.com>
             Subject: SMTP e-mail test
             This is a test mail sender."""
    r, d = conn.login(sender, port)
    print('Login reply: {0}'.format(r))
    
    print('--- Sending an email...')
    result = "Mail sent successfully"
    try:
        conn.sendmail(sender, receivers, msg)
    except SMTPRecipientsRefused, e:
        result = "All recipients were refused"
    except SMTPHeloError, e:
        result = "The server didn’t reply properly to the HELO greeting"
    except SMTPSenderRefused, e:
        result = "The server didn’t accept the from_addr"
    except SMTPDataError, e:
        result = ("The server replied with an unexpected error code "
                 + "(other than a refusal of a recipient).")
    else:
        pass
    conn.close()
    print('--- Done!')
    return result
