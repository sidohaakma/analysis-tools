#!python

import rest

from utils.arguments import Arguments

PROJECT = 'lifecycle'

def createProject(admin_username, admin_password, host, project):
    data = "{\"name\":\"" + PROJECT + "\",\"title\":\"" + PROJECT + "\",\"description\":\"" + PROJECT + "\",\"database\":\"opal_data\",\"vcfStoreService\": null}"

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

    print(u'\u2714' + ' bootstrap project: lifecycle')
