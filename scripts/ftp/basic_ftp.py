import os
import sys
import logging
import getpass
import datetime

from hashlib import md5

from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed

class DummyMD5Authorizer(DummyAuthorizer):

    def validate_authentication(self, username, password, handler):
        if sys.version_info >= (3, 0):
            password = md5(password.encode('latin1'))
        hash = password.hexdigest()
        try:
            if self.user_table[username]['pwd'] != hash:
                raise KeyError
        except KeyError:
            raise AuthenticationFailed

def main():

    passcode = getpass.getpass('Enter the ftp access code:')

    hash = md5(passcode.encode('latin1')).hexdigest()

    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyMD5Authorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user('dylan', hash, '/home/dylan/Videos', perm='elradfmwMT')
    # authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # changing log line prefix
    current_time = datetime.datetime.now().strftime('%m-%d %H:%M:%S')
    handler.log_prefix = current_time + ' [%(username)s]@%(remote_ip)s'

    logging.basicConfig(filename='/var/log/pyftpd/pyftpd.log', level=logging.INFO)

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('0.0.0.0', 2211)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()

