#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """Generates a .tgz archive from the web_static folder contents"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        archive_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except FolderDoesNotExist:
        return None
