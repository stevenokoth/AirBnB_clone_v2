#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.237.45.220', '54.237.63.152']


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


def do_deploy(archive_path):
    """Deploys an archive on the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        archive_name = archive_path.split("/")[-1]
        min_ext = archive_name.split(".")[0]
        dest = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(dest, min_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive_name, dest, min_ext))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(dest, min_ext))
        run('rm -rf {}{}/web_static'.format(dest, min_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(dest, min_ext))
        return True
    except PathNotFound:
        return False


def deploy():
    """Creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
