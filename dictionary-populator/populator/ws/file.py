#!python

import opal.file
import constants

from utils.arguments import Arguments

UPLOAD_CLIENT_PATH = 'dictionaries'

def uploadFile(admin_username, admin_password, host, version, dictionary):
    
    opal.file.do_command(Arguments({
        'user': admin_username,
        'password': admin_password,
        'content_type': 'multipart/form-data',
        'opal': host,
        'path': constants.UPLOAD_PATH,
        'upload': UPLOAD_CLIENT_PATH+ '/'  + version + '_' + dictionary + '.zip',
        'verbose': False,
        'download': '',
        'json': False
    }))

    print(u'\u2714' + ' upload metadata-file for table: ' + version + '_'  + dictionary)