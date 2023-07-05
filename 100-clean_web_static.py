#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that
deletes out-of-date archives, using the function do_clean
"""
from fabric.api import *


env.hosts = ['54.237.45.220', '54.237.63.152']
env.user = "ubuntu"


def do_clean(number=0):
    """Deletes out-of-date archives"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    dir = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(dir, number))
