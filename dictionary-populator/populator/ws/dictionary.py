#!python

import constants
import opal.import_xml

from utils.arguments import Arguments

def importDictionary(admin_username, admin_password, host, version, dictionary):
    opal.import_xml.do_command(Arguments({
        'user': admin_username,
        'password': admin_password,
        'opal': host,
        'path': constants.UPLOAD_PATH + '/' + version + '_' + dictionary + '.zip',
        'destination': constants.PROJECT,
        'tables': '',
        'separator': ',',
        'type': 'Participant',
        'incremental': False,
        'limit': 0,
        'identifiers': '',
        'policy': '',
        'quote': '"',
        'firstRow': '1',
        'characterSet': 'ISO-8859-1',
        'valueType': '',
        'verbose': False,
        'json': False
    }))

    print(u'\u2714' + ' bootstrap metadata for table: ' + version + '_' + dictionary)