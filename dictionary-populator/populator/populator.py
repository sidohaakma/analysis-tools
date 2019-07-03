#!python

import click
import ws.constants

from ws.project import createProject
from ws.file import uploadFile
from ws.dictionary import importDictionary

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
    '--version',
    '-v', 
    default='1_0',
    help='Version of data dictionary; can be x_x, for example 1_0.')
def populate(host, admin_username, admin_password, version): 
    '''
    This script will bootstrap the data dictionary version of the LifeCycle variables into Opal.
    '''

    createProject(admin_username, admin_password, host)

    uploadFile(admin_username, admin_password, host, version, ws.constants.DICT_MONTHLY_REPEATED_MEASURES)
    uploadFile(admin_username, admin_password, host, version, ws.constants.DICT_YEARLY_REPEATED_MEASURES)
    uploadFile(admin_username, admin_password, host, version, ws.constants.DICT_NON_REPEATED_MEASURES)

    importDictionary(admin_username, admin_password, host, version, ws.constants.DICT_MONTHLY_REPEATED_MEASURES)
    importDictionary(admin_username, admin_password, host, version, ws.constants.DICT_YEARLY_REPEATED_MEASURES)
    importDictionary(admin_username, admin_password, host, version, ws.constants.DICT_NON_REPEATED_MEASURES)
