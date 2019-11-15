from io import BytesIO
from datetime import datetime, timedelta
import pysftp


class FTP(object):

    SFTP_CONNECTION_OPTIONS = {
        'host'      : '127.0.0.1',
        'port'      : 22,
        'username'  : 'USERNAME',
        'password'  : 'secret',
    }

    DEST_DIR = '/Inbox'

    def __init__(self, dest_dir=None):
        self.client = self.connect()
        if dest_dir: self.DEST_DIR = dest_dir
        self.chdir(self.DEST_DIR)

    def __del__(self):
        self.disconnect()

    def connect(self):
        print("connecting FTP")
        self.SFTP_CONNECTION_OPTIONS['cnopts'] = self.SFTP_CONNECTION_OPTIONS.get('cnopts', pysftp.CnOpts())
        self.SFTP_CONNECTION_OPTIONS['cnopts'].hostkeys = None
        cinfo = self.SFTP_CONNECTION_OPTIONS
        return pysftp.Connection(**cinfo)

    def disconnect(self):
        if not self.client: return
        print("disconnecting FTP")
        self.client.close()

    def chdir(self, path):
        self.client.chdir(path)

    def list(self):
        return self.client.listdir()

    def read(self, file_name):
        file = BytesIO()
        self.client.getfo(file_name, file)
        return file

