#!python

import opal.rest
import opal.file
import opal.import_xml

import click
import constants
import ws.rest

from arguments import Arguments

@click.command()
@click.option(
    '--host',
    '-h', 
    prompt=True,
    default='localhost:8080',
    help='Opal host; only yhe dns name, without protocol and port number.')
@click.option(
    '--admin-username',
    '-u', 
    default='administrator',
    help='Administrator username of Opal host')
@click.option(
    '--admin-password',
    '-p', 
    prompt=True,
    help='Administrator password of Opal host')
@click.option(
    '--cohort',
    '-c', 
    prompt=True,
    help='Cohort name; lowercase for example "gecko".')
@click.option(
    '--version',
    '-v', 
    default='1_0',
    help='Version of data dictionary; can be x_x, for example 1_0.')
@click.option(
    '--status',
    '-s', 
    default='beta',
    help='Status of data dictionary; can be beta or released.')        
def populate(host, admin_username, admin_password, cohort, version, status): 
    '''
    This script will bootstrap the data dictionary version of the LifeCycle variables into Opal.
    '''

    data = "{\"name\":\"" + constants.PROJECT_PREFIX + cohort + "\",\"title\":\"" + constants.PROJECT_PREFIX + cohort + "\",\"description\":\"" + constants.PROJECT_PREFIX + cohort + "\",\"database\":\"opal_data\",\"vcfStoreService\": null}"

    args_project_bootstrap = Arguments({
        'headers': '',
        'user': admin_username,
        'password': admin_password,
        'content_type': 'application/json',
        'opal': host,
        'accept': 'application/json',
        'method': 'POST',
        'content': data,
        'ws': '/projects',
        'verbose': False,
        'json': False
    })

    ws.rest.do_command(args_project_bootstrap)

    print(u'\u2714' + ' bootstrap project: lifecycle_' + cohort)

    opal.file.do_command(Arguments({
        'user': admin_username,
        'password': admin_password,
        'content_type': 'multipart/form-data',
        'opal': host,
        'path': constants.UPLOAD_PATH,
        'upload': constants.UPLOAD_CLIENT_PATH+ '/'  + version + '_' + constants.DICT_MONTHLY_REPEATED_MEASURES + '.zip',
        'verbose': False,
        'download': '',
        'json': False
    }))

    print(u'\u2714' + ' upload metadata-file for table: ' + version + '_' + constants.DICT_MONTHLY_REPEATED_MEASURES)

    opal.file.do_command(Arguments({
        'user': admin_username,
        'password': admin_password,
        'content_type': 'multipart/form-data',
        'opal': host,
        'path': constants.UPLOAD_PATH,
        'upload': constants.UPLOAD_CLIENT_PATH+ '/'  + version + '_' + constants.DICT_YEARLY_REPEATED_MEASURES + '.zip',
        'verbose': False,
        'download': '',
        'json': False
    }))

    print(u'\u2714' + ' upload metadata-file for table: ' + version + '_' + constants.DICT_YEARLY_REPEATED_MEASURES)

    opal.file.do_command(Arguments({
        'user': admin_username,
        'password': admin_password,
        'content_type': 'multipart/form-data',
        'opal': host,
        'path': constants.UPLOAD_PATH,
        'upload': constants.UPLOAD_CLIENT_PATH + '/' + version + '_' + constants.DICT_NON_REPEATED_MEASURES + '.zip',
        'verbose': False,
        'download': '',
        'json': False
    }))
    print(u'\u2714' + ' upload metadata-file for table: ' + version + '_' + constants.DICT_NON_REPEATED_MEASURES)

    
    
    
    opal.import_xml.do_command(Arguments({
        'user': admin_username,
        'password': admin_password,
        'opal': host,
        'path': constants.UPLOAD_PATH + '/' + version + '_' + constants.DICT_MONTHLY_REPEATED_MEASURES + '.zip',
        'destination': constants.PROJECT_PREFIX + cohort,
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
    print(u'\u2714' + ' bootstrap metadata for table: ' + version + '_' + status + '_' + constants.DICT_MONTHLY_REPEATED_MEASURES)
    
    opal.import_xml.do_command(Arguments({
        'user': admin_username,
        'password': admin_password,
        'opal': host,
        'path': constants.UPLOAD_PATH + '/' + version + '_' + constants.DICT_YEARLY_REPEATED_MEASURES + '.zip',
        'destination': constants.PROJECT_PREFIX + cohort,
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
    print(u'\u2714' + ' bootstrap metadata for table: ' + version + '_' + status + '_' + constants.DICT_YEARLY_REPEATED_MEASURES)
    
    opal.import_xml.do_command(Arguments({
        'user': admin_username,
        'password': admin_password,
        'opal': host,
        'path': constants.UPLOAD_PATH + '/' + version + '_' + constants.DICT_NON_REPEATED_MEASURES + '.zip',
        'destination': constants.PROJECT_PREFIX + cohort,
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

    print(u'\u2714' + ' bootstrap metadata for table: ' + version + '_' + status + '_' + constants.DICT_NON_REPEATED_MEASURES)
    