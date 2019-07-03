#!python

import rest
import constants

from utils.arguments import Arguments

def createProject(admin_username, admin_password, host):
    data = "{\"name\":\"" + constants.PROJECT + "\",\"title\":\"" + constants.PROJECT + "\",\"description\":\"" + constants.PROJECT + "\",\"database\":\"opal_data\",\"vcfStoreService\": null}"

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

    rest.do_command(args_project_bootstrap)

    print(u'\u2714' + ' bootstrap project: ' + constants.PROJECT)
